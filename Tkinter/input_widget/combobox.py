"""
combobox设置值与获取值
"""
import tkinter as tk
from tkinter import ttk

def show_selected_value():
    value = combo.get()
    print("Selected Value:", value)

root = tk.Tk()

combo = ttk.Combobox(root, values=('Option 1', 'Option 2', 'Option 3'))

# 设置下拉框的初始值
combo.current(1)  # 默认选择第一个选项

combo.pack()

button = tk.Button(root, text="Get Value", command=show_selected_value)
button.pack()

root.mainloop()
