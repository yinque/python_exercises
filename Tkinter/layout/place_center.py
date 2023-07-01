"""
子组件使用place布局相对于父组件居中
"""

import tkinter as tk

root = tk.Tk()

# 创建一个居中的标签
label = tk.Label(root, text="居中文本")
label.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
