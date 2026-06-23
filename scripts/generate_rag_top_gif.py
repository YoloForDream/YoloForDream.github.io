from PIL import Image, ImageDraw, ImageFont
import math
import os

# Configuration
WIDTH = 1920
HEIGHT = 288
FRAMES = 60
DURATION = 100  # ms per frame

def generate_rag_top_gif():
    frames = []
    
    # Try to load font, fallback to default
    try:
        font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)
        font_small = ImageFont.truetype('/Library/Fonts/Arial.ttf', 24)
    except:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    for frame in range(FRAMES):
        img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 10, 30))
        draw = ImageDraw.Draw(img)
        
        # Draw background grid
        for i in range(0, WIDTH, 60):
            alpha = 0.1 + 0.1 * math.sin(frame * 0.05 + i * 0.01)
            draw.line([(i, 0), (i, HEIGHT)], fill=(int(79*alpha), int(172*alpha), int(254*alpha)))
        for i in range(0, HEIGHT, 40):
            alpha = 0.1 + 0.1 * math.sin(frame * 0.05 + i * 0.02)
            draw.line([(0, i), (WIDTH, i)], fill=(int(79*alpha), int(172*alpha), int(254*alpha)))
        
        # Main title "RAG vs Agentic RAG"
        title_x = WIDTH // 2
        title_y = HEIGHT // 2 - 30
        
        # Draw RAG text (left side)
        rag_color = (0, 242, 254)
        rag_offset = int(10 * math.sin(frame * 0.1))
        draw.text((title_x - 180 + rag_offset, title_y), "RAG", fill=rag_color, font=font)
        
        # Draw VS symbol
        vs_scale = 1 + 0.1 * math.sin(frame * 0.2)
        vs_color = (255, 107, 0)
        draw.text((title_x - 40, title_y - 5), "VS", fill=vs_color, font=font)
        
        # Draw Agentic RAG text (right side)
        agentic_color = (155, 89, 182)
        agentic_offset = int(-10 * math.sin(frame * 0.1))
        draw.text((title_x + 60 + agentic_offset, title_y), "Agentic RAG", fill=agentic_color, font=font)
        
        # Draw sub-title
        subtitle_y = title_y + 50
        draw.text((title_x, subtitle_y), "A Comparative Analysis", fill=(200, 200, 200), font=font_small, anchor='mm')
        
        # Draw RAG icon (left - traditional)
        rag_icon_x = WIDTH // 4
        rag_icon_y = HEIGHT // 2
        
        # Draw flow arrows for RAG
        for i in range(4):
            node_x = rag_icon_x - 80 + i * 50
            node_y = rag_icon_y
            node_alpha = 0.5 + 0.5 * math.sin(frame * 0.15 + i)
            draw.ellipse([node_x-15, node_y-15, node_x+15, node_y+15], 
                         fill=(int(79*node_alpha), int(172*node_alpha), int(254*node_alpha)))
            if i < 3:
                arrow_alpha = 0.3 + 0.3 * math.sin(frame * 0.2 + i)
                draw.line([(node_x+15, node_y), (node_x+35, node_y)], 
                          fill=(int(200*arrow_alpha), int(200*arrow_alpha), int(200*arrow_alpha)), width=2)
                draw.polygon([(node_x+35, node_y-3), (node_x+42, node_y), (node_x+35, node_y+3)], 
                             fill=(int(200*arrow_alpha), int(200*arrow_alpha), int(200*arrow_alpha)))
        
        # Draw Agentic RAG icon (right - circular)
        agentic_icon_x = WIDTH * 3 // 4
        agentic_icon_y = HEIGHT // 2
        
        # Draw circular reasoning loop
        loop_radius = 40
        loop_alpha = 0.6 + 0.4 * math.sin(frame * 0.1)
        draw.ellipse([agentic_icon_x-loop_radius, agentic_icon_y-loop_radius,
                      agentic_icon_x+loop_radius, agentic_icon_y+loop_radius],
                     fill=None, outline=(int(155*loop_alpha), int(89*loop_alpha), int(182*loop_alpha)), width=3)
        
        # Draw rotating arrow around the loop
        arrow_angle = frame * 0.1
        arrow_x = agentic_icon_x + int(loop_radius * math.cos(arrow_angle))
        arrow_y = agentic_icon_y + int(loop_radius * math.sin(arrow_angle))
        draw.polygon([(arrow_x, arrow_y),
                      (arrow_x - 8*math.cos(arrow_angle+0.5) - 5*math.sin(arrow_angle+0.5),
                       arrow_y - 8*math.sin(arrow_angle+0.5) + 5*math.cos(arrow_angle+0.5)),
                      (arrow_x - 8*math.cos(arrow_angle+0.5) + 5*math.sin(arrow_angle+0.5),
                       arrow_y - 8*math.sin(arrow_angle+0.5) - 5*math.cos(arrow_angle+0.5))],
                     fill=(255, 107, 0))
        
        # Draw center dot
        draw.ellipse([agentic_icon_x-8, agentic_icon_y-8, agentic_icon_x+8, agentic_icon_y+8],
                     fill=(155, 89, 182))
        
        # Draw floating particles
        for i in range(20):
            px = (i * 97 + frame * 13) % WIDTH
            py = (i * 53 + frame * 7) % HEIGHT
            particle_alpha = 0.3 + 0.3 * math.sin(frame * 0.05 + i)
            draw.ellipse([px-2, py-2, px+2, py+2], 
                         fill=(int(0*particle_alpha), int(242*particle_alpha), int(254*particle_alpha)))
        
        frames.append(img)
    
    # Save GIF
    output_path = 'assets/images/posts/rag-vs-agentic-rag-comparative-analysis/top.gif'
    frames[0].save(output_path, save_all=True, append_images=frames[1:], 
                   duration=DURATION, loop=0, optimize=False)
    print(f"Generated top.gif at {output_path}")

if __name__ == '__main__':
    os.makedirs('assets/images/posts/rag-vs-agentic-rag-comparative-analysis', exist_ok=True)
    generate_rag_top_gif()
    print("Done!")
