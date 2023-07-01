"""
获取默认字体信息
https://tkdocs.com/tutorial/fonts.html
"""
import tkinter as tk
from tkinter.font import Font

# 创建默认的根窗口
root = tk.Tk()

# 创建一个默认字体对象
default_font = Font()

# 获取默认字体的名称和大小
font_family = default_font.actual()['family']
font_size = default_font.actual()['size']
print(f"默认字体名称：{font_family}")
print(f"默认字体大小：{font_size}")

# 获取字体的度量信息
metrics = default_font.metrics()

# 打印字体的度量信息
print("Ascent:", metrics["ascent"],"(px)")
print("Descent:", metrics["descent"],"(px)")
print("Line Space:", metrics["linespace"],"(px)")

# 测量字体
text_width = default_font.measure("Hello world")
print(f"'Hello world'文本长度: {text_width}px")

# 运行主事件循环
root.mainloop()

