from PIL import Image, ImageDraw

width, height = 1920, 288
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
for x in range(0, width, 96):
    draw.line([(x, 0), (x, height)], fill=(30, 58, 90), width=1)
for y in range(0, height, 48):
    draw.line([(0, y), (width, y)], fill=(30, 58, 90), width=1)

# 左侧：神经网络/AI处理
cx1, cy1 = 400, height//2
for i in range(3):
    for j in range(4):
        nx = cx1 - 90 + i * 60
        ny = cy1 - 60 + j * 35
        draw.ellipse([nx-8, ny-8, nx+8, ny+8], fill=(79, 172, 254))
        if i < 2:
            draw.line([(nx, ny), (nx+60, ny)], fill=(79, 172, 254), width=1)
        if j < 3:
            draw.line([(nx, ny), (nx, ny+35)], fill=(79, 172, 254), width=1)
draw.text((cx1-45, cy1+70), "AI Processing", fill=(79, 172, 254))

# 中间：Agentic AI核心
cx2, cy2 = 960, height//2
points = [(cx2, cy2-70), (cx2+60, cy2-35), (cx2+60, cy2+35), (cx2, cy2+70), (cx2-60, cy2+35), (cx2-60, cy2-35)]
draw.polygon(points, outline=(0, 242, 254), width=2)
draw.ellipse([cx2-35, cy2-35, cx2+35, cy2+35], outline=(79, 172, 254), width=2)
draw.ellipse([cx2-20, cy2-20, cx2+20, cy2+20], outline=(0, 242, 254), width=1)
draw.ellipse([cx2-5, cy2-5, cx2+5, cy2+5], fill=(0, 242, 254))
draw.text((cx2-70, cy2+90), "AGENTIC AI", fill=(0, 242, 254))
draw.text((cx2-65, cy2+110), "Smart Manufacturing", fill=(79, 172, 254))

# 右侧：工厂控制
cx3, cy3 = 1520, height//2
draw.rectangle([cx3-70, cy3-60, cx3+70, cy3+60], fill=(26, 58, 90), outline=(79, 172, 254))
for i in range(3):
    for j in range(2):
        rx = cx3-40 + i * 35
        ry = cy3-30 + j * 40
        draw.rectangle([rx-12, ry-10, rx+12, ry+10], fill=(13, 40, 64), outline=(79, 172, 254))
        if i == 0:
            draw.ellipse([rx-4, ry-4, rx+4, ry+4], fill=(79, 172, 254))
        elif i == 1:
            draw.line([rx-5, ry, rx+5, ry], fill=(79, 172, 254), width=2)
            draw.line([rx, ry-5, rx, ry+5], fill=(79, 172, 254), width=2)
        else:
            draw.polygon([(rx, ry-6), (rx+6, ry+6), (rx-6, ry+6)], fill=(79, 172, 254))
draw.text((cx3-45, cy3+80), "Factory Control", fill=(79, 172, 254))

# 连接线
draw.line([(520, cy1), (800, cy2)], fill=(79, 172, 254), width=2)
draw.line([(1120, cy2), (1400, cy3)], fill=(0, 242, 254), width=2)

# 装饰元素
for i in range(5):
    px = 100 + i * 350
    py = 50 + (i % 2) * 180
    draw.ellipse([px-3, py-3, px+3, py+3], fill=(79, 172, 254))

img.save('/Users/reywang/Desktop/YoloForDream.github.io/assets/images/posts/agentic-ai-in-manufacturing-practical-analysis/top.jpg')
print('Image created successfully!')