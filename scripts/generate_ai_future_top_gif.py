from PIL import Image, ImageDraw, ImageFont
import math
import os

# Configuration
WIDTH = 1920
HEIGHT = 288
FRAMES = 60
DURATION = 80  # ms per frame

def generate_ai_future_gif():
    frames = []
    
    # Try to load font, fallback to default
    try:
        font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 48)
        font_small = ImageFont.truetype('/Library/Fonts/Arial.ttf', 24)
    except:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    for frame in range(FRAMES):
        img = Image.new('RGB', (WIDTH, HEIGHT), color=(5, 5, 20))
        draw = ImageDraw.Draw(img)
        
        # Draw grid background with moving lines
        for i in range(0, WIDTH, 80):
            wave_offset = int(10 * math.sin(frame * 0.05 + i * 0.01))
            alpha = 0.15 + 0.1 * math.sin(frame * 0.03 + i * 0.01)
            draw.line([(i, 0), (i + wave_offset, HEIGHT)], 
                      fill=(int(0*alpha), int(242*alpha), int(254*alpha)))
        for i in range(0, HEIGHT, 40):
            alpha = 0.1 + 0.05 * math.sin(frame * 0.05 + i * 0.02)
            draw.line([(0, i), (WIDTH, i)], 
                      fill=(int(155*alpha), int(89*alpha), int(182*alpha)))
        
        # Draw main AI text
        ai_text = "AI"
        ai_x = WIDTH // 2 - 80
        ai_y = HEIGHT // 2
        
        # Glowing effect for AI
        glow_radius = 20 + int(10 * math.sin(frame * 0.1))
        for r in range(glow_radius, 0, -5):
            alpha = (1 - r/glow_radius) * 0.3
            draw.text((ai_x + r*0.5, ai_y), ai_text, 
                      fill=(int(0*alpha), int(242*alpha), int(254*alpha)), 
                      font=font)
        
        # Main AI text with gradient effect
        ai_color = (0, 242, 254)
        text_offset = int(3 * math.sin(frame * 0.15))
        draw.text((ai_x + text_offset, ai_y - 20), ai_text, fill=ai_color, font=font)
        
        # Draw subtitle "TECHNOLOGY & FUTURE"
        sub_text = "TECHNOLOGY & FUTURE"
        sub_x = WIDTH // 2
        sub_y = ai_y + 50
        sub_alpha = 0.7 + 0.3 * math.sin(frame * 0.1)
        draw.text((sub_x, sub_y), sub_text, 
                  fill=(int(255*sub_alpha), int(107*sub_alpha), int(0*sub_alpha)), 
                  font=font_small, anchor='mm')
        
        # Draw neural network nodes
        nn_nodes = []
        for layer in range(3):
            for node in range(5):
                nx = 150 + layer * 200 + int(30 * math.sin(frame * 0.05 + layer + node))
                ny = HEIGHT // 2 - 80 + node * 40 + int(10 * math.sin(frame * 0.1 + node))
                nn_nodes.append((nx, ny))
                node_alpha = 0.4 + 0.4 * math.sin(frame * 0.15 + layer * 2 + node)
                draw.ellipse([nx-8, ny-8, nx+8, ny+8], 
                             fill=(int(0*node_alpha), int(242*node_alpha), int(254*node_alpha)))
        
        # Draw neural network connections
        for i in range(len(nn_nodes)):
            for j in range(i+1, len(nn_nodes)):
                if abs(i - j) <= 5:
                    conn_alpha = 0.1 + 0.1 * math.sin(frame * 0.1 + i + j)
                    draw.line([nn_nodes[i], nn_nodes[j]], 
                              fill=(int(155*conn_alpha), int(89*conn_alpha), int(182*conn_alpha)), 
                              width=1)
        
        # Draw floating particles
        for i in range(30):
            px = (i * 67 + frame * 17) % WIDTH
            py = (i * 43 + frame * 13) % HEIGHT
            particle_alpha = 0.4 + 0.4 * math.sin(frame * 0.05 + i)
            particle_size = 2 + int(2 * math.sin(frame * 0.1 + i))
            draw.ellipse([px-particle_size, py-particle_size, 
                          px+particle_size, py+particle_size], 
                         fill=(int(0*particle_alpha), int(242*particle_alpha), int(254*particle_alpha)))
        
        # Draw robot icon on the right
        robot_x = WIDTH - 200
        robot_y = HEIGHT // 2
        
        # Robot head
        draw.ellipse([robot_x-30, robot_y-40, robot_x+30, robot_y-10], 
                     fill=(100, 150, 200), outline=(0, 242, 254), width=2)
        # Robot eyes
        eye_offset = int(5 * math.sin(frame * 0.2))
        draw.ellipse([robot_x-15+eye_offset, robot_y-30, robot_x-8+eye_offset, robot_y-23], 
                     fill=(0, 242, 254))
        draw.ellipse([robot_x+8+eye_offset, robot_y-30, robot_x+15+eye_offset, robot_y-23], 
                     fill=(0, 242, 254))
        # Robot body
        draw.rectangle([robot_x-25, robot_y-10, robot_x+25, robot_y+30], 
                       fill=(80, 130, 180), outline=(0, 242, 254), width=2)
        # Robot antenna
        draw.line([(robot_x, robot_y-45), (robot_x, robot_y-55)], 
                  fill=(100, 150, 200), width=3)
        antenna_glow = int(10 * math.sin(frame * 0.3))
        draw.ellipse([robot_x-3+antenna_glow, robot_y-58, robot_x+3+antenna_glow, robot_y-52], 
                     fill=(255, 107, 0))
        
        # Draw circuit board pattern on the left
        circuit_x = 100
        circuit_y = HEIGHT // 2
        
        # Circuit lines
        for i in range(5):
            line_y = circuit_y - 60 + i * 30
            draw.line([(circuit_x-50, line_y), (circuit_x+50, line_y)], 
                      fill=(79, 172, 254), width=2)
            if i % 2 == 0:
                draw.line([(circuit_x, line_y), (circuit_x, line_y + 15)], 
                          fill=(79, 172, 254), width=2)
        
        # Circuit nodes
        for i in range(3):
            for j in range(4):
                cx = circuit_x - 30 + i * 30
                cy = circuit_y - 45 + j * 30
                node_pulse = 3 + int(3 * math.sin(frame * 0.2 + i + j))
                draw.ellipse([cx-node_pulse, cy-node_pulse, cx+node_pulse, cy+node_pulse], 
                             fill=(0, 242, 254))
        
        # Draw binary code stream on the right side
        binary_y = (frame * 8) % (HEIGHT + 100) - 50
        for i in range(8):
            binary_text = '0' if (i + frame) % 2 == 0 else '1'
            binary_alpha = 0.3 + 0.3 * math.sin(frame * 0.1 + i)
            draw.text((WIDTH - 30, binary_y + i * 40), binary_text, 
                      fill=(int(0*binary_alpha), int(242*binary_alpha), int(254*binary_alpha)), 
                      font=font_small)
        
        frames.append(img)
    
    # Save GIF
    output_path = 'assets/images/top.gif'
    frames[0].save(output_path, save_all=True, append_images=frames[1:], 
                   duration=DURATION, loop=0, optimize=False)
    print(f"Generated {output_path}")

if __name__ == '__main__':
    generate_ai_future_gif()
    print("Done!")
