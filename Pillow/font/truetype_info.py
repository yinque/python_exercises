"""
打开字体文件xxx.ttf，显示该文件的字体信息
"""

from PIL import ImageFont

# 指定字体文件路径
font_file = 'comici.ttf'

# 使用ImageFont.TrueType加载字体文件
font = ImageFont.truetype(font_file)
# 获取字体的名称
font_name = font.getname()[0]

print(font_name)
