from PIL import Image, ImageDraw, ImageFont
import os

# Create output directory
output_dir = 'assets/images/posts/rag-vs-agentic-rag-comparative-analysis'
os.makedirs(output_dir, exist_ok=True)

# Generate Traditional RAG Architecture image
def generate_traditional_rag():
    width, height = 800, 400
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Font
    try:
        font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 14)
    except:
        font = ImageFont.load_default()
    
    # Nodes
    nodes = [
        ("User Question", 100, 100),
        ("Vectorization", 250, 100),
        ("Retrieval", 400, 100),
        ("Top-K Docs", 550, 100),
        ("Context", 400, 200),
        ("Generate\nAnswer", 250, 300)
    ]
    
    # Draw nodes
    for label, x, y in nodes:
        draw.ellipse([x-40, y-25, x+40, y+25], fill=(79, 172, 254), outline=(0, 102, 204), width=2)
        draw.text((x, y), label, fill='white', font=font, anchor='mm')
    
    # Draw arrows
    draw.line([(140, 100), (210, 100)], fill=(100, 100, 100), width=3)
    draw.polygon([(210, 95), (220, 100), (210, 105)], fill=(100, 100, 100))
    
    draw.line([(290, 100), (360, 100)], fill=(100, 100, 100), width=3)
    draw.polygon([(360, 95), (370, 100), (360, 105)], fill=(100, 100, 100))
    
    draw.line([(440, 100), (510, 100)], fill=(100, 100, 100), width=3)
    draw.polygon([(510, 95), (520, 100), (510, 105)], fill=(100, 100, 100))
    
    draw.line([(550, 125), (550, 175)], fill=(100, 100, 100), width=3)
    draw.polygon([(545, 175), (550, 185), (555, 175)], fill=(100, 100, 100))
    
    draw.line([(400, 125), (400, 175)], fill=(100, 100, 100), width=3)
    draw.polygon([(395, 175), (400, 185), (405, 175)], fill=(100, 100, 100))
    
    draw.line([(400, 225), (290, 275)], fill=(100, 100, 100), width=3)
    draw.polygon([(290, 275), (300, 280), (293, 285)], fill=(100, 100, 100))
    
    # Title
    draw.text((400, 370), "Traditional RAG Architecture", fill=(50, 50, 50), font=font, anchor='mm')
    
    img.save(f'{output_dir}/traditional-rag.png')
    print("Generated traditional-rag.png")

# Generate Agentic RAG Architecture image
def generate_agentic_rag():
    width, height = 800, 450
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Font
    try:
        font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 14)
    except:
        font = ImageFont.load_default()
    
    # Center reasoning loop
    cx, cy = 400, 200
    
    # Draw main agent node
    draw.ellipse([cx-60, cy-40, cx+60, cy+40], fill=(0, 242, 254), outline=(0, 150, 150), width=2)
    draw.text((cx, cy), "Reasoning\nLoop", fill='white', font=font, anchor='mm')
    
    # Outer nodes
    outer_nodes = [
        ("User\nQuestion", cx-250, cy-80),
        ("Retrieval\nAgent", cx-150, cy+120),
        ("Dynamic\nRetrieval", cx+150, cy+120),
        ("Execute/\nGenerate", cx+250, cy-80),
        ("Reflect\n& Correct", cx, cy+180)
    ]
    
    for label, x, y in outer_nodes:
        draw.ellipse([x-40, y-25, x+40, y+25], fill=(155, 89, 182), outline=(100, 50, 120), width=2)
        draw.text((x, y), label, fill='white', font=font, anchor='mm')
    
    # Draw arrows (circular flow)
    draw.line([(cx-190, cy-80), (cx-100, cy-60)], fill=(100, 100, 100), width=3)
    draw.polygon([(cx-100, cy-60), (cx-90, cy-57), (cx-97, cy-50)], fill=(100, 100, 100))
    
    draw.line([(cx-110, cy+80), (cx-40, cy+60)], fill=(100, 100, 100), width=3)
    draw.polygon([(cx-40, cy+60), (cx-33, cy+53), (cx-30, cy+60)], fill=(100, 100, 100))
    
    draw.line([(cx+40, cy+60), (cx+110, cy+80)], fill=(100, 100, 100), width=3)
    draw.polygon([(cx+110, cy+80), (cx+117, cy+73), (cx+110, cy+67)], fill=(100, 100, 100))
    
    draw.line([(cx+190, cy-80), (cx+100, cy-60)], fill=(100, 100, 100), width=3)
    draw.polygon([(cx+100, cy-60), (cx+107, cy-53), (cx+100, cy-47)], fill=(100, 100, 100))
    
    draw.line([(cx, cy+140), (cx, cy+155)], fill=(100, 100, 100), width=3)
    draw.polygon([(cx, cy+155), (cx-5, cy+165), (cx+5, cy+165)], fill=(100, 100, 100))
    
    draw.line([(cx-60, cy), (cx-110, cy-20)], fill=(100, 100, 100), width=3)
    draw.polygon([(cx-110, cy-20), (cx-120, cy-15), (cx-113, cy-8)], fill=(100, 100, 100))
    
    # Title
    draw.text((400, 420), "Agentic RAG Architecture", fill=(50, 50, 50), font=font, anchor='mm')
    
    img.save(f'{output_dir}/agentic-rag.png')
    print("Generated agentic-rag.png")

if __name__ == '__main__':
    generate_traditional_rag()
    generate_agentic_rag()
    print("All images generated successfully!")
