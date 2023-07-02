"""
打开字体文件xxx.ttf，显示该文件的字体信息
windows可以用，其它的就自己找一个字体文件路径替换吧
"""
from fontTools.ttLib import TTFont

font_file = 'C:\\Windows\\Fonts\\arial.ttf'  # 字体文件路径

# 打开字体文件
font = TTFont(font_file)

# 获取字体的名称信息
name_table = font['name']
family_name = name_table.getDebugName(1)  # 字体族名称
style_name = name_table.getDebugName(2)  # 字体样式名称

# 打印字体信息
print("字体族名称:", family_name)
print("字体样式名称:", style_name)

# 关闭字体文件
font.close()
