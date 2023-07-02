"""
打开字体文件xxx.ttf，显示该文件的字体信息
"""

from PIL import ImageFont

# 指定字体文件路径
font_file = 'comici.ttf'

# 使用ImageFont.TrueType加载字体文件
font = ImageFont.truetype(font_file)
# 字体信息
print(font.getname())
# 字体的名称
print(font.getname()[0])
# 字体样式，bold、italic等
print(font.getname()[1])
