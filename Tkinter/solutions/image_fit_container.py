"""
图片自适应容器，
如果宽大于最大宽度，缩小到最大宽度
如果高大于最大高度，缩小到最大高度
"""

import tkinter as tk
from tkinter.font import Font

from PIL import ImageTk, Image, ImageFont


class ImageBox(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # 定义容器宽高
        self.width = 400
        self.height = 200
        # width=self.width, height=self.height,
        super().__init__(parent, width=self.width, height=self.height, bg="gray", *args, **kwargs)
        # Label的宽高的单位是字体大小em，定义的宽高单位是px，需要进行一些转换
        default_font = Font()
        fw = default_font.measure("M")
        fh = default_font.metrics()["linespace"]
        w, h = int(self.width / fw), int(self.height / fh)
        self.label = tk.Label(self)
        self.label.propagate(False)
        self.set_img("../_resource/pattern.png")
        self.label.place(relx=0.5, rely=0.5, anchor="center")
        self.pack()

    def set_img(self, img_path):
        image = Image.open(img_path)
        # 重新设置宽高
        max_width = self.width
        max_height = self.height

        w, h = image.size
        if w > max_width:
            scale = max_width / w
            w, h = max_width, int(h * scale)
            image = image.resize((w, h))
        if h > max_height:
            scale = max_height / h
            w, h = int(w * scale), max_height
            image = image.resize((w, h))
        photo = ImageTk.PhotoImage(image)
        self.label.config(image=photo)
        self.label.image = photo  # important! 保持对图片对象的引用，否则会触发垃圾回收不显示图片


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        ImageBox(self)


if __name__ == '__main__':
    app = App()
    app.mainloop()
