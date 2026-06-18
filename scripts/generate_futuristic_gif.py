from PIL import Image, ImageDraw
import math

# 创建 GIF 帧
frames = []
width, height = 1920, 288

for frame in range(30):
    img = Image.new('RGB', (width, height), color=(8, 8, 16))
    draw = ImageDraw.Draw(img)
    
    # 动态渐变背景
    for y in range(height):
        ratio = y / height
        wave = math.sin(frame * 0.1 + y * 0.02) * 10
        r = int(8 + ratio * 12 + wave)
        g = int(8 + ratio * 18 + wave)
        b = int(16 + ratio * 24 + wave)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # 动态网格
    grid_spacing = 60 + int(10 * math.sin(frame * 0.2))
    for x in range(0, width, grid_spacing):
        alpha = 0.2 + 0.3 * math.sin(frame * 0.3 + x * 0.01)
        draw.line([(x, 0), (x, height)], fill=(int(50*alpha), int(100*alpha), int(150*alpha)), width=1)
    for y in range(0, height, grid_spacing):
        alpha = 0.2 + 0.3 * math.sin(frame * 0.3 + y * 0.02)
        draw.line([(0, y), (width, y)], fill=(int(50*alpha), int(100*alpha), int(150*alpha)), width=1)
    
    # 左侧：数据流动
    for i in range(6):
        dx = 150 + i * 80
        for j in range(4):
            dy = 60 + j * 45
            node_alpha = 0.5 + 0.5 * math.sin(frame * 0.4 + i + j)
            draw.ellipse([dx-6, dy-6, dx+6, dy+6], fill=(int(79*node_alpha), int(172*node_alpha), int(254*node_alpha)))
            if i < 5:
                flow_alpha = 0.3 + 0.4 * math.sin(frame * 0.6 + i * 0.5)
                draw.line([(dx, dy), (dx+80, dy)], fill=(int(79*flow_alpha), int(172*flow_alpha), int(254*flow_alpha)), width=2)
    
    # 中间：AI 处理器核心
    cx, cy = width // 2, height // 2
    
    # 外圈六边形
    hex_points = [(cx, cy-80), (cx+69, cy-40), (cx+69, cy+40), (cx, cy+80), (cx-69, cy+40), (cx-69, cy-40)]
    hex_alpha = 0.5 + 0.5 * math.sin(frame * 0.2)
    draw.polygon(hex_points, outline=(int(0*hex_alpha), int(242*hex_alpha), int(254*hex_alpha)), width=2)
    
    # 旋转的内圈
    for ring in range(3):
        ring_radius = 30 + ring * 15
        ring_alpha = 0.3 + 0.3 * math.sin(frame * 0.3 + ring)
        draw.ellipse([cx-ring_radius, cy-ring_radius, cx+ring_radius, cy+ring_radius], 
                    outline=(int(79*ring_alpha), int(172*ring_alpha), int(254*ring_alpha)), width=1)
    
    # 旋转的数据轨道
    for i in range(12):
        angle = (frame * 10 + i * 30) % 360
        rad = math.radians(angle)
        px = cx + int(50 * math.cos(rad))
        py = cy + int(50 * math.sin(rad))
        orbit_alpha = 0.6 + 0.4 * math.sin(frame * 0.5 + i)
        draw.ellipse([px-3, py-3, px+3, py+3], fill=(int(0*orbit_alpha), int(242*orbit_alpha), int(254*orbit_alpha)))
    
    # 中心核心
    core_pulse = 10 + int(5 * math.sin(frame * 0.5))
    draw.ellipse([cx-core_pulse, cy-core_pulse, cx+core_pulse, cy+core_pulse], fill=(0, 242, 254))
    
    # 右侧：电路板/芯片
    chip_x, chip_y = 1650, height // 2
    draw.rectangle([chip_x-60, chip_y-50, chip_x+60, chip_y+50], fill=(15, 30, 50), outline=(79, 172, 254))
    
    # 芯片元件
    for row in range(3):
        for col in range(4):
            ex = chip_x-40 + col * 25
            ey = chip_y-30 + row * 25
            comp_alpha = 0.4 + 0.6 * math.sin(frame * 0.4 + row + col)
            if (row + col) % 2 == 0:
                draw.ellipse([ex-5, ey-5, ex+5, ey+5], fill=(int(79*comp_alpha), int(172*comp_alpha), int(254*comp_alpha)))
            else:
                draw.rectangle([ex-5, ey-5, ex+5, ey+5], fill=(int(0*comp_alpha), int(242*comp_alpha), int(254*comp_alpha)))
    
    # 连接线
    conn_alpha = 0.5 + 0.5 * math.sin(frame * 0.3)
    draw.line([(450, cy), (cx-80, cy)], fill=(int(79*conn_alpha), int(172*conn_alpha), int(254*conn_alpha)), width=2)
    draw.line([(cx+80, cy), (1550, cy)], fill=(int(0*conn_alpha), int(242*conn_alpha), int(254*conn_alpha)), width=2)
    
    # 数据流粒子
    for i in range(8):
        particle_x = 450 + (1100 / 8) * i + (frame * 5) % 1100
        if particle_x < 1550:
            draw.ellipse([particle_x-2, cy-2, particle_x+2, cy+2], fill=(0, 242, 254))
    
    # 发光装饰点
    for i in range(15):
        px = 50 + i * 125
        py = 30 if i % 2 == 0 else height - 30
        glow_alpha = 0.3 + 0.7 * math.sin(frame * 0.5 + i * 0.5)
        draw.ellipse([px-2, py-2, px+2, py+2], fill=(int(79*glow_alpha), int(172*glow_alpha), int(254*glow_alpha)))
    
    frames.append(img)

# 保存为 GIF
gif_path = '/Users/reywang/Desktop/YoloForDream.github.io/assets/images/top.gif'
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=50, loop=0)
print('Futuristic GIF created successfully!')