from PIL import Image, ImageDraw

# 创建灰度图像对象
image_size = (256, 256)
image = Image.new("L", image_size)
draw = ImageDraw.Draw(image)

# 绘制灰度渐变
for x in range(image_size[0]):
    for y in range(image_size[1]):
        grayscale_values = x    # 灰度值从0-255，越大像素点越亮（白）
        draw.point((x, y), grayscale_values)

# 保存图像
image.show("gray_gradient.png")
