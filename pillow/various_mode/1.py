from PIL import Image, ImageDraw

# 创建1位图像对象
image_size = (256, 256)
image = Image.new("1", image_size, color=1)
draw = ImageDraw.Draw(image)

# 绘制黑白相间的背景
block_size = image_size[0] // 3

for i in range(3):
    for j in range(3):
        if (i + j) % 2 == 0:
            draw.rectangle([(i * block_size, j * block_size), ((i + 1) * block_size, (j + 1) * block_size)], fill=0)

# 显示图像
image.show("black_white_background.bmp")
