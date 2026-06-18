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
    
    # 左侧：神经网络
    cx1, cy1 = 400, height//2
    for i in range(3):
        for j in range(4):
            nx = cx1 - 90 + i * 60
            ny = cy1 - 60 + j * 35
            pulse = 8 + int(3 * math.sin(frame * 0.5 + i + j))
            draw.ellipse([nx-pulse, ny-pulse, nx+pulse, ny+pulse], fill=(79, 172, 254))
            if i < 2:
                draw.line([(nx, ny), (nx+60, ny)], fill=(79, 172, 254), width=1)
            if j < 3:
                draw.line([(nx, ny), (nx, ny+35)], fill=(79, 172, 254), width=1)
    
    # 中间：Agentic AI 核心
    cx2, cy2 = 960, height//2
    points = [(cx2, cy2-70), (cx2+60, cy2-35), (cx2+60, cy2+35), (cx2, cy2+70), (cx2-60, cy2+35), (cx2-60, cy2-35)]
    draw.polygon(points, outline=(0, 242, 254), width=2)
    
    pulse_size = 35 + int(5 * math.sin(frame * 0.3))
    draw.ellipse([cx2-pulse_size, cy2-pulse_size, cx2+pulse_size, cy2+pulse_size], outline=(79, 172, 254), width=2)
    draw.ellipse([cx2-20, cy2-20, cx2+20, cy2+20], outline=(0, 242, 254), width=1)
    
    core_pulse = 5 + int(3 * math.sin(frame * 0.5))
    draw.ellipse([cx2-core_pulse, cy2-core_pulse, cx2+core_pulse, cy2+core_pulse], fill=(0, 242, 254))
    
    # 右侧：工厂控制
    cx3, cy3 = 1520, height//2
    draw.rectangle([cx3-70, cy3-60, cx3+70, cy3+60], fill=(26, 58, 90), outline=(79, 172, 254))
    for i in range(3):
        for j in range(2):
            rx = cx3-40 + i * 35
            ry = cy3-30 + j * 40
            draw.rectangle([rx-12, ry-10, rx+12, ry+10], fill=(13, 40, 64), outline=(79, 172, 254))
            if i == 0:
                blink = math.sin(frame * 0.8 + i + j) > 0
                draw.ellipse([rx-4, ry-4, rx+4, ry+4], fill=(79, 172, 254) if blink else (30, 58, 90))
            elif i == 1:
                draw.line([rx-5, ry, rx+5, ry], fill=(79, 172, 254), width=2)
                draw.line([rx, ry-5, rx, ry+5], fill=(79, 172, 254), width=2)
            else:
                draw.polygon([(rx, ry-6), (rx+6, ry+6), (rx-6, ry+6)], fill=(79, 172, 254))
    
    # 连接线
    line_alpha = 0.5 + 0.5 * math.sin(frame * 0.3)
    draw.line([(520, cy1), (800, cy2)], fill=(int(79*line_alpha), int(172*line_alpha), int(254*line_alpha)), width=2)
    draw.line([(1120, cy2), (1400, cy3)], fill=(int(0*line_alpha), int(242*line_alpha), int(254*line_alpha)), width=2)
    
    # 装饰元素
    for i in range(8):
        px = 100 + i * 220
        py = 30 + (i % 2) * 200
        star_size = 2 + int(2 * math.sin(frame * 0.5 + i))
        draw.ellipse([px-star_size, py-star_size, px+star_size, py+star_size], fill=(79, 172, 254))
    
    frames.append(img)

# 保存为 GIF
gif_path = '/Users/reywang/Desktop/YoloForDream.github.io/assets/images/posts/agentic-ai-in-manufacturing-practical-analysis/top.gif'
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=80, loop=0)
print('Top GIF created successfully!')