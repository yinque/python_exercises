def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# 带异常处理
try:
    result = divide(10, 0)
except ValueError as e:
    print("捕获到异常:", e)
else:
    print("结果:", result)

# 无异常处理
# result = divide(10, 0)
# print("结果:", result)

# 总结
# 当使用try...catch捕获异常时，异常将不会被抛出（在控制台显示红字），而是自己处理