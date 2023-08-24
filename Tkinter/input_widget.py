import tkinter as tk

# 创建窗口
window = tk.Tk()

# 创建控件
label1 = tk.Label(window, text="Label 1")
label2 = tk.Label(window, text="Label 2")
button = tk.Button(window, text="Button")

# 布局控件
label1.place(x=50, y=50)
label2.place(x=100, y=100)
button.place(x=150, y=150)


# 运行窗口
window.mainloop()
