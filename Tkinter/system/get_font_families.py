import tkinter as tk
import tkinter.font as font

root = tk.Tk()

# 获取系统中所有的字体族
font_families = font.families()

# 打印所有字体族
for font_family in font_families:
    print(font_family)

root.mainloop()
