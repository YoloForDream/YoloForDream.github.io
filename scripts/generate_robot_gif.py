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
    grid_spacing = 60
    for x in range(0, width, grid_spacing):
        alpha = 0.2 + 0.3 * math.sin(frame * 0.3 + x * 0.01)
        draw.line([(x, 0), (x, height)], fill=(int(50*alpha), int(100*alpha), int(150*alpha)), width=1)
    for y in range(0, height, grid_spacing):
        alpha = 0.2 + 0.3 * math.sin(frame * 0.3 + y * 0.02)
        draw.line([(0, y), (width, y)], fill=(int(50*alpha), int(100*alpha), int(150*alpha)), width=1)
    
    # 左侧：机器人图标
    robot_x, robot_y = 300, height // 2
    
    # 机器人头部
    head_offset = int(5 * math.sin(frame * 0.5))
    draw.rectangle([robot_x-30, robot_y-60+head_offset, robot_x+30, robot_y-30+head_offset], 
                  fill=(79, 172, 254), outline=(0, 242, 254))
    
    # 机器人眼睛
    eye_glow = 0.5 + 0.5 * math.sin(frame * 0.3)
    draw.ellipse([robot_x-15, robot_y-50+head_offset, robot_x-8, robot_y-43+head_offset], 
                 fill=(int(0*eye_glow), int(242*eye_glow), int(254*eye_glow)))
    draw.ellipse([robot_x+8, robot_y-50+head_offset, robot_x+15, robot_y-43+head_offset], 
                 fill=(int(0*eye_glow), int(242*eye_glow), int(254*eye_glow)))
    
    # 机器人天线
    draw.line([(robot_x, robot_y-60+head_offset), (robot_x, robot_y-80+head_offset)], fill=(79, 172, 254), width=3)
    antenna_pulse = 3 + int(3 * math.sin(frame * 0.8))
    draw.ellipse([robot_x-antenna_pulse, robot_y-85+head_offset, robot_x+antenna_pulse, robot_y-75+head_offset], 
                 fill=(0, 242, 254))
    
    # 机器人身体
    draw.rectangle([robot_x-25, robot_y-30, robot_x+25, robot_y+30], 
                  fill=(50, 100, 150), outline=(79, 172, 254))
    
    # 机器人手臂
    arm_angle = math.sin(frame * 0.4) * 0.3
    draw.line([(robot_x-25, robot_y-10), (robot_x-55, robot_y+20)], fill=(79, 172, 254), width=6)
    draw.line([(robot_x+25, robot_y-10), (robot_x+55, robot_y+20)], fill=(79, 172, 254), width=6)
    
    # 机器人腿部
    draw.line([(robot_x-15, robot_y+30), (robot_x-15, robot_y+60)], fill=(79, 172, 254), width=6)
    draw.line([(robot_x+15, robot_y+30), (robot_x+15, robot_y+60)], fill=(79, 172, 254), width=6)
    
    # 中间：AI 文字和核心
    cx, cy = width // 2, height // 2
    
    # "AGENTIC AI" 文字 - 向上移动，增加与下方轮子的距离
    text_alpha = 0.8 + 0.2 * math.sin(frame * 0.3)
    draw.text((cx-120, cy-100), "AGENTIC AI", fill=(int(0*text_alpha), int(242*text_alpha), int(254*text_alpha)), font_size=36)
    draw.text((cx-100, cy-60), "INTELLIGENT SYSTEMS", fill=(int(79*text_alpha), int(172*text_alpha), int(254*text_alpha)), font_size=18)
    
    # 六边形框架 - 向下移动
    hex_points = [(cx, cy-30), (cx+26, cy-15), (cx+26, cy+15), (cx, cy+30), (cx-26, cy+15), (cx-26, cy-15)]
    hex_alpha = 0.5 + 0.5 * math.sin(frame * 0.2)
    draw.polygon(hex_points, outline=(int(0*hex_alpha), int(242*hex_alpha), int(254*hex_alpha)), width=2)
    
    # 旋转的 AI 符号
    for i in range(6):
        angle = (frame * 12 + i * 60) % 360
        rad = math.radians(angle)
        px = cx + int(20 * math.cos(rad))
        py = cy + int(20 * math.sin(rad))
        draw.ellipse([px-3, py-3, px+3, py+3], fill=(79, 172, 254))
    
    # 中心脉冲
    core_pulse = 6 + int(3 * math.sin(frame * 0.5))
    draw.ellipse([cx-core_pulse, cy-core_pulse, cx+core_pulse, cy+core_pulse], fill=(0, 242, 254))
    
    # 右侧：数据流可视化
    data_x, data_y = 1600, height // 2
    
    # 柱状图
    for bar in range(5):
        bar_height = 60 + int(40 * math.sin(frame * 0.3 + bar * 0.5))
        bar_alpha = 0.6 + 0.4 * math.sin(frame * 0.4 + bar)
        bottom_y = data_y + 30
        top_y = data_y + 30 - bar_height
        draw.rectangle([data_x-80 + bar * 30, min(bottom_y, top_y), data_x-60 + bar * 30, max(bottom_y, top_y)], 
                      fill=(int(79*bar_alpha), int(172*bar_alpha), int(254*bar_alpha)))
    
    # 数据流箭头
    arrow_offset = (frame * 8) % 100
    draw.polygon([(data_x-120 + arrow_offset, data_y), (data_x-110 + arrow_offset, data_y-5), (data_x-110 + arrow_offset, data_y+5)], 
                 fill=(0, 242, 254))
    
    # 连接线
    conn_alpha = 0.5 + 0.5 * math.sin(frame * 0.3)
    draw.line([(360, cy), (cx-60, cy)], fill=(int(79*conn_alpha), int(172*conn_alpha), int(254*conn_alpha)), width=2)
    draw.line([(cx+60, cy), (1500, cy)], fill=(int(0*conn_alpha), int(242*conn_alpha), int(254*conn_alpha)), width=2)
    
    # 数据粒子
    for i in range(6):
        particle_x = 360 + (1140 / 6) * i + (frame * 6) % 1140
        if particle_x < 1500:
            draw.ellipse([particle_x-2, cy-2, particle_x+2, cy+2], fill=(0, 242, 254))
    
    # 装饰元素
    for i in range(12):
        px = 80 + i * 150
        py = 30 if i % 2 == 0 else height - 30
        glow_alpha = 0.3 + 0.7 * math.sin(frame * 0.5 + i * 0.5)
        draw.ellipse([px-2, py-2, px+2, py+2], fill=(int(79*glow_alpha), int(172*glow_alpha), int(254*glow_alpha)))
    
    frames.append(img)

# 保存为 GIF
gif_path = '/Users/reywang/Desktop/YoloForDream.github.io/assets/images/top.gif'
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=50, loop=0)
print('Robot GIF created successfully!')