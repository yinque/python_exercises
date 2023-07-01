"""
使用Label显示图片
"""

import tkinter as tk
from PIL import ImageTk, Image

# 创建 tkinter 窗口
root = tk.Tk()

# 加载图片
image = Image.open("../_resource/pattern.png")
photo = ImageTk.PhotoImage(image)

# 创建 Label，并设置图片
label = tk.Label(root, image=photo)
label.pack()

# 运行窗口主循环
root.mainloop()
