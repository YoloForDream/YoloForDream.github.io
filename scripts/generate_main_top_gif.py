from PIL import Image, ImageDraw
import math

# 创建 GIF 帧
frames = []
width, height = 1920, 288

for frame in range(24):
    img = Image.new('RGB', (width, height), color=(10, 10, 26))
    draw = ImageDraw.Draw(img)
    
    # 绘制渐变背景
    for y in range(height):
        ratio = y / height
        r = int(10 + ratio * 10)
        g = int(10 + ratio * 15)
        b = int(26 + ratio * 20)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # 绘制网格线
    grid_alpha = 0.3 + 0.2 * math.sin(frame * 0.3)
    for x in range(0, width, 96):
        draw.line([(x, 0), (x, height)], fill=(int(30*grid_alpha), int(58*grid_alpha), int(90*grid_alpha)), width=1)
    for y in range(0, height, 48):
        draw.line([(0, y), (width, y)], fill=(int(30*grid_alpha), int(58*grid_alpha), int(90*grid_alpha)), width=1)
    
    # 中心 AI 大脑图案
    cx, cy = width // 2, height // 2
    
    # 外圈旋转节点
    for i in range(8):
        angle = (frame * 15 + i * 45) % 360
        rad = math.radians(angle)
        nx = cx + int(100 * math.cos(rad))
        ny = cy + int(100 * math.sin(rad))
        size = 12 + int(4 * math.sin(frame * 0.5 + i))
        draw.ellipse([nx-size, ny-size, nx+size, ny+size], fill=(79, 172, 254))
        draw.line([(cx, cy), (nx, ny)], fill=(79, 172, 254), width=2)
    
    # 中层圆环
    pulse_size = 60 + int(8 * math.sin(frame * 0.3))
    draw.ellipse([cx-pulse_size, cy-pulse_size, cx+pulse_size, cy+pulse_size], outline=(0, 242, 254), width=2)
    
    # 内层圆环
    draw.ellipse([cx-35, cy-35, cx+35, cy+35], outline=(79, 172, 254), width=1)
    
    # 中心核心
    core_pulse = 8 + int(4 * math.sin(frame * 0.5))
    draw.ellipse([cx-core_pulse, cy-core_pulse, cx+core_pulse, cy+core_pulse], fill=(0, 242, 254))
    
    # 装饰元素
    for i in range(10):
        px = 80 + i * 180
        py = 40 + (i % 2) * 200
        star_size = 2 + int(2 * math.sin(frame * 0.5 + i))
        draw.ellipse([px-star_size, py-star_size, px+star_size, py+star_size], fill=(79, 172, 254))
    
    frames.append(img)

# 保存为 GIF
gif_path = '/Users/reywang/Desktop/YoloForDream.github.io/assets/images/top.gif'
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=80, loop=0)
print('Main top GIF created successfully!')