"""
保存文件功能
"""
import tkinter as tk
from tkinter import filedialog


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", tk.END))
            print("File saved successfully.")


root = tk.Tk()

text = tk.Text(root)
text.pack()

button = tk.Button(root, text="Save", command=save_file)
button.pack()

root.mainloop()
