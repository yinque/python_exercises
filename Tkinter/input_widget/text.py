"""
输入框控件，数据绑定
"""

import tkinter as tk

def update_variable():
    value = text.get("1.0", "end-1c")  # 获取Text控件中的文本
    var.set(value)  # 更新绑定的变量的值

root = tk.Tk()

var = tk.StringVar()
var.set("Hello, world!")

text = tk.Text(root)
text.insert("1.0", var.get())  # 将绑定的变量的值插入到Text控件中
text.pack()

button = tk.Button(root, text="Update", command=update_variable)
button.pack()

root.mainloop()