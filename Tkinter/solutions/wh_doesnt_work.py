"""
解决容器宽高 不显示的问题。
pack布局会自动修改父容器大小，
导致 width=100, height=100 父容器的不生效
使用 place 布局解决这个问题
"""

import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root, width=100, height=100, bg="gray")
frame.pack()

label = tk.Label(frame,text="Hello", bg="red")

# 问题示例
# label.pack() # 使用这个会导致父容器width=100, height=100失效
#

# 解决方案
label.place(x=0, y=0)
#

root.mainloop()
