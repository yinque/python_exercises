from PIL import Image

# 图像大小和颜色设置
width = 800
height = 200
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]  # 彩虹颜色

# 创建彩虹图像
image = Image.new('RGB', (width, height))

# 绘制彩虹图像
pixel_data = []
for x in range(width):
    for y in range(height):
        color_index = x * len(colors) // width
        pixel_data.append(colors[color_index])

image.putdata(pixel_data)

# 展示图像
image.show()
