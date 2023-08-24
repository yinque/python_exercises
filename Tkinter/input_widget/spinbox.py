import tkinter as tk
from tkinter import ttk

root = tk.Tk()

spinbox = ttk.Spinbox(root, from_=0, to=100)
spinbox.set(50)     # 设置默认值
spinbox.pack()

root.mainloop()
