import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # 打开图片文件，创建标签并显示图片
        image = Image.open("pattern.png")
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(self, image=photo)
        label.image = photo  # important! 保持对图片对象的引用，否则会触发垃圾回收不显示图片
        label.pack()


if __name__ == '__main__':
    app = App()
    app.mainloop()
