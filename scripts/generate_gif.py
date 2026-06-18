from PIL import Image, ImageDraw
import math

# 创建 GIF 帧
frames = []
width, height = 400, 300

for frame in range(12):
    img = Image.new('RGB', (width, height), color=(10, 10, 26))
    draw = ImageDraw.Draw(img)
    
    # 绘制渐变背景
    for y in range(height):
        ratio = y / height
        r = int(10 + ratio * 10)
        g = int(10 + ratio * 15)
        b = int(26 + ratio * 20)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # 绘制 AI 大脑图案
    cx, cy = width // 2, height // 2
    for i in range(5):
        angle = (frame * 30 + i * 72) % 360
        rad = math.radians(angle)
        nx = cx + int(80 * math.cos(rad))
        ny = cy + int(80 * math.sin(rad))
        size = 15 + int(5 * math.sin(frame * 0.5 + i))
        draw.ellipse([nx-size, ny-size, nx+size, ny+size], fill=(79, 172, 254))
        draw.line([(cx, cy), (nx, ny)], fill=(79, 172, 254), width=2)
    
    # 中心圆
    pulse_size = 40 + int(10 * math.sin(frame * 0.5))
    draw.ellipse([cx-pulse_size, cy-pulse_size, cx+pulse_size, cy+pulse_size], outline=(0, 242, 254), width=2)
    draw.ellipse([cx-15, cy-15, cx+15, cy+15], fill=(0, 242, 254))
    
    frames.append(img)

# 保存为 GIF
gif_path = '/Users/reywang/Desktop/YoloForDream.github.io/assets/images/posts/agentic-ai-in-manufacturing-practical-analysis/ai-animation.gif'
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=100, loop=0)
print('GIF created successfully!')