"""
监听所有输入事件，带防抖
"""
import threading
import tkinter as tk


# 为app添加所有输入事件
def listen_input(app: tk.Tk):
    # 防抖等待时间（秒）
    debounce_wait_time = 0.2
    # 计时器
    last_timer: threading.Timer = None

    def debounce_handler(*args, **kwargs):
        nonlocal last_timer
        if last_timer is not None:
            last_timer.cancel()
        last_timer = threading.Timer(debounce_wait_time, handle_input, args=args, kwargs=kwargs)
        last_timer.start()

    counter = 0

    def handle_input(event):
        # print(f"Event Type: {event.type}")
        # print(f"Event Keysym: {event.keysym}")
        # print(f"Event Keycode: {event.keycode}")
        nonlocal counter
        print(counter)
        counter += 1

    app.bind_all("<Key>", debounce_handler)  # 绑定所有键盘事件
    app.bind_all("<Button>", debounce_handler)  # 绑定所有鼠标按钮事件
    app.bind_all("<MouseWheel>", debounce_handler)  # 绑定滚轮事件


root = tk.Tk()

listen_input(root)

root.mainloop()
