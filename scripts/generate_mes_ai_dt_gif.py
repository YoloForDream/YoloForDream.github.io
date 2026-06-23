from PIL import Image, ImageDraw
import math

# 创建 GIF 帧
frames = []
width, height = 1920, 288

for frame in range(30):
    img = Image.new('RGB', (width, height), color=(8, 10, 25))
    draw = ImageDraw.Draw(img)
    
    # 动态渐变背景
    for y in range(height):
        ratio = y / height
        wave = math.sin(frame * 0.1 + y * 0.02) * 8
        r = int(8 + ratio * 10 + wave)
        g = int(10 + ratio * 15 + wave)
        b = int(25 + ratio * 20 + wave)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # 动态网格线
    grid_alpha = 0.2 + 0.3 * math.sin(frame * 0.3)
    for x in range(0, width, 80):
        draw.line([(x, 0), (x, height)], fill=(int(40*grid_alpha), int(80*grid_alpha), int(120*grid_alpha)), width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(int(40*grid_alpha), int(80*grid_alpha), int(120*grid_alpha)), width=1)
    
    # ==================== 左侧：MES 制造执行系统 ====================
    mes_x, mes_y = 250, height // 2
    
    # MES 图标 - 工业机器人手臂（制造行业标准图标）
    # 机器人底座
    draw.rectangle([mes_x-35, mes_y+30, mes_x+35, mes_y+50], fill=(50, 80, 120), outline=(79, 172, 254))
    
    # 机器人手臂关节1
    arm1_angle = math.sin(frame * 0.3) * 0.3
    arm1_length = 40
    arm1_end_x = mes_x + int(arm1_length * math.cos(-0.5 + arm1_angle))
    arm1_end_y = mes_y + 30 + int(arm1_length * math.sin(-0.5 + arm1_angle))
    draw.line([(mes_x, mes_y+30), (arm1_end_x, arm1_end_y)], fill=(79, 172, 254), width=8)
    
    # 机器人手臂关节2
    arm2_angle = math.sin(frame * 0.4) * 0.4
    arm2_length = 35
    arm2_end_x = arm1_end_x + int(arm2_length * math.cos(-1.5 + arm2_angle))
    arm2_end_y = arm1_end_y + int(arm2_length * math.sin(-1.5 + arm2_angle))
    draw.line([(arm1_end_x, arm1_end_y), (arm2_end_x, arm2_end_y)], fill=(0, 242, 254), width=6)
    
    # 机械爪/末端执行器
    claw_spread = 8 + int(4 * math.sin(frame * 0.5))
    draw.line([(arm2_end_x, arm2_end_y), (arm2_end_x - claw_spread, arm2_end_y + 10)], fill=(79, 172, 254), width=4)
    draw.line([(arm2_end_x, arm2_end_y), (arm2_end_x + claw_spread, arm2_end_y + 10)], fill=(79, 172, 254), width=4)
    
    # 控制面板/数据显示
    draw.rectangle([mes_x-50, mes_y-50, mes_x+50, mes_y-10], fill=(20, 40, 60), outline=(79, 172, 254))
    # 显示屏幕
    draw.rectangle([mes_x-40, mes_y-40, mes_x+40, mes_y-20], fill=(10, 20, 35), outline=(0, 242, 254))
    # 数据指示灯
    for i in range(5):
        light_alpha = 0.3 + 0.7 * math.sin(frame * 0.5 + i)
        lx = mes_x - 30 + i * 15
        ly = mes_y - 28
        draw.ellipse([lx-3, ly-3, lx+3, ly+3], fill=(int(0*light_alpha), int(242*light_alpha), int(254*light_alpha)))
    
    # 文字
    draw.text((mes_x-45, mes_y+70), "MES", fill=(0, 242, 254), font_size=24)
    draw.text((mes_x-60, mes_y+95), "Manufacturing Execution System", fill=(79, 172, 254), font_size=12)
    
    # ==================== 中间：AI 人工智能 ====================
    ai_x, ai_y = width // 2, height // 2
    
    # AI 大脑/神经网络图案
    # 外圈节点
    for i in range(8):
        angle = (frame * 15 + i * 45) % 360
        rad = math.radians(angle)
        nx = ai_x + int(60 * math.cos(rad))
        ny = ai_y + int(60 * math.sin(rad))
        node_size = 8 + int(4 * math.sin(frame * 0.5 + i))
        draw.ellipse([nx-node_size, ny-node_size, nx+node_size, ny+node_size], fill=(0, 242, 254))
        draw.line([(ai_x, ai_y), (nx, ny)], fill=(79, 172, 254), width=2)
    
    # 内圈节点
    for i in range(4):
        angle = (frame * 20 + i * 90 + 22) % 360
        rad = math.radians(angle)
        nx = ai_x + int(35 * math.cos(rad))
        ny = ai_y + int(35 * math.sin(rad))
        draw.ellipse([nx-5, ny-5, nx+5, ny+5], fill=(79, 172, 254))
    
    # 中心脉冲
    core_pulse = 10 + int(5 * math.sin(frame * 0.4))
    draw.ellipse([ai_x-core_pulse, ai_y-core_pulse, ai_x+core_pulse, ai_y+core_pulse], fill=(0, 242, 254))
    core_ring = 20 + int(5 * math.sin(frame * 0.3))
    draw.ellipse([ai_x-core_ring, ai_y-core_ring, ai_x+core_ring, ai_y+core_ring], outline=(0, 242, 254), width=2)
    
    # 文字
    draw.text((ai_x-35, ai_y+80), "AI", fill=(0, 242, 254), font_size=28)
    draw.text((ai_x-65, ai_y+105), "Artificial Intelligence", fill=(79, 172, 254), font_size=12)
    
    # ==================== 右侧：DT 数字孪生 ====================
    dt_x, dt_y = 1670, height // 2
    
    # DT 数字孪生图标 - 虚拟与现实的镜像映射
    # 外圈光晕
    halo_alpha = 0.3 + 0.3 * math.sin(frame * 0.3)
    draw.ellipse([dt_x-60, dt_y-60, dt_x+60, dt_y+60], outline=(int(0*halo_alpha), int(242*halo_alpha), int(254*halo_alpha)), width=2)
    draw.ellipse([dt_x-75, dt_y-45, dt_x+75, dt_y+45], outline=(int(79*halo_alpha), int(172*halo_alpha), int(254*halo_alpha)), width=1)
    
    # 物理实体（下方）
    # 立方体代表物理资产
    draw.polygon([(dt_x-35, dt_y+10), (dt_x+10, dt_y-5), (dt_x+10, dt_y+30), (dt_x-35, dt_y+45)], 
                 fill=(30, 60, 100), outline=(79, 172, 254))
    draw.polygon([(dt_x-10, dt_y-5), (dt_x+35, dt_y-20), (dt_x+35, dt_y+15), (dt_x-10, dt_y+30)], 
                 fill=(40, 80, 130), outline=(79, 172, 254))
    draw.line([(dt_x-35, dt_y+10), (dt_x-10, dt_y-5)], fill=(79, 172, 254))
    draw.line([(dt_x+10, dt_y-5), (dt_x+35, dt_y-20)], fill=(79, 172, 254))
    draw.line([(dt_x+10, dt_y+30), (dt_x+35, dt_y+15)], fill=(79, 172, 254))
    draw.line([(dt_x-35, dt_y+45), (dt_x-10, dt_y+30)], fill=(79, 172, 254))
    
    # 虚拟模型（上方）- 半透明表示虚拟
    virtual_alpha = 0.6 + 0.3 * math.sin(frame * 0.2)
    draw.polygon([(dt_x-35, dt_y-15), (dt_x+10, dt_y-30), (dt_x+10, dt_y+5), (dt_x-35, dt_y+20)], 
                 fill=(int(0*virtual_alpha*0.3), int(242*virtual_alpha*0.3), int(254*virtual_alpha*0.3)), 
                 outline=(int(0*virtual_alpha), int(242*virtual_alpha), int(254*virtual_alpha)))
    draw.polygon([(dt_x-10, dt_y-30), (dt_x+35, dt_y-45), (dt_x+35, dt_y-10), (dt_x-10, dt_y+5)], 
                 fill=(int(79*virtual_alpha*0.3), int(172*virtual_alpha*0.3), int(254*virtual_alpha*0.3)), 
                 outline=(int(79*virtual_alpha), int(172*virtual_alpha), int(254*virtual_alpha)))
    
    # 镜像连接线（虚实对应）
    for i in range(3):
        line_alpha = 0.5 + 0.5 * math.sin(frame * 0.4 + i)
        px1 = dt_x - 20 + i * 20
        draw.line([(px1, dt_y+10), (px1, dt_y-15)], fill=(int(0*line_alpha), int(242*line_alpha), int(254*line_alpha)), width=2)
    
    # 数据流箭头（从物理到虚拟）
    arrow_y = dt_y + ((frame * 5) % 25)
    draw.polygon([(dt_x, arrow_y), (dt_x-5, arrow_y-8), (dt_x+5, arrow_y-8)], fill=(0, 242, 254))
    
    # 数据点在虚实之间流动
    for i in range(4):
        flow_y = dt_y - 15 + ((dt_y + 10 - (dt_y - 15)) * (frame * 8 + i * 30) % 100) / 100
        draw.ellipse([dt_x-3, flow_y-3, dt_x+3, flow_y+3], fill=(0, 242, 254))
    
    # 文字
    draw.text((dt_x-40, dt_y+60), "DT", fill=(0, 242, 254), font_size=28)
    draw.text((dt_x-65, dt_y+85), "Digital Twin", fill=(79, 172, 254), font_size=12)
    
    # ==================== 连接线和数据流 ====================
    # MES -> AI 连接线
    conn_alpha = 0.4 + 0.6 * math.sin(frame * 0.3)
    draw.line([(mes_x+70, mes_y), (ai_x-70, ai_y)], fill=(int(79*conn_alpha), int(172*conn_alpha), int(254*conn_alpha)), width=3)
    
    # AI -> DT 连接线
    draw.line([(ai_x+70, ai_y), (dt_x-80, dt_y)], fill=(int(0*conn_alpha), int(242*conn_alpha), int(254*conn_alpha)), width=3)
    
    # 数据流动粒子
    for i in range(8):
        # MES -> AI 方向
        pos1 = ((ai_x - 70) - (mes_x + 70)) * ((frame * 8 + i * 40) % 400) / 400 + (mes_x + 70)
        if pos1 < ai_x - 70:
            draw.ellipse([pos1-3, ai_y-3, pos1+3, ai_y+3], fill=(0, 242, 254))
        
        # AI -> DT 方向
        pos2 = ((dt_x - 80) - (ai_x + 70)) * ((frame * 8 + i * 40) % 400) / 400 + (ai_x + 70)
        if pos2 < dt_x - 80:
            draw.ellipse([pos2-3, dt_y-3, pos2+3, dt_y+3], fill=(0, 242, 254))
    
    # 箭头指示
    arrow1_x = mes_x + 70 + ((ai_x - 70 - mes_x - 70) * (frame * 5) % 100) / 100
    draw.polygon([(arrow1_x, ai_y), (arrow1_x+8, ai_y-4), (arrow1_x+8, ai_y+4)], fill=(0, 242, 254))
    
    arrow2_x = ai_x + 70 + ((dt_x - 80 - ai_x - 70) * (frame * 5) % 100) / 100
    draw.polygon([(arrow2_x, dt_y), (arrow2_x+8, dt_y-4), (arrow2_x+8, dt_y+4)], fill=(0, 242, 254))
    
    # ==================== 装饰元素 ====================
    # 顶部发光点
    for i in range(15):
        px = 100 + i * 120
        glow_alpha = 0.3 + 0.7 * math.sin(frame * 0.5 + i * 0.3)
        draw.ellipse([px-2, 25-2, px+2, 25+2], fill=(int(79*glow_alpha), int(172*glow_alpha), int(254*glow_alpha)))
    
    # 底部发光点
    for i in range(15):
        px = 100 + i * 120
        glow_alpha = 0.3 + 0.7 * math.sin(frame * 0.5 + i * 0.3 + 1)
        draw.ellipse([px-2, height-25-2, px+2, height-25+2], fill=(int(79*glow_alpha), int(172*glow_alpha), int(254*glow_alpha)))
    
    frames.append(img)

# 创建目录并保存 GIF
import os
gif_dir = '/Users/reywang/Desktop/YoloForDream.github.io/assets/images/posts/mes-ai-dt-fusion-system'
os.makedirs(gif_dir, exist_ok=True)

gif_path = os.path.join(gif_dir, 'top.gif')
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=50, loop=0)
print(f'MES-AI-DT GIF created successfully at: {gif_path}')
