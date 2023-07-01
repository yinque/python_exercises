"""
父组件获取子组件列表
"""
import tkinter as tk

root = tk.Tk()

# 创建一些子组件
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
button = tk.Button(root, text="Button")

# 将子组件添加到应用程序中
label1.pack()
label2.pack()
button.pack()

# 获取应用程序下的所有子组件
children = root.winfo_children()

# 遍历
for child in children:
    print(child)

root.mainloop()
