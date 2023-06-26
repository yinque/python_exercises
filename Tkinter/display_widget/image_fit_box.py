"""
图片自适应容器，
如果宽大于最大宽度，缩小到最大宽度
如果高大于最大高度，缩小到最大高度
"""

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        image = Image.open("pattern.png")
        # 重新设置宽高
        max_height = 200
        max_width = 400
        w, h = image.size
        if w > max_width:
            scale = max_width/w
            w, h = max_width, int(h * scale)
            image = image.resize((w, h))
        if h > max_height:
            scale = max_height/h
            w, h = int(w * scale), max_height
            image = image.resize((w, h))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(self, image=photo)
        label.image = photo  # important! 保持对图片对象的引用，否则会触发垃圾回收不显示图片
        label.pack()


if __name__ == '__main__':
    app = App()
    app.mainloop()
