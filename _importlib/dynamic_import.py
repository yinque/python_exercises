# 从./pkg/mod.py动态导入文件
# mod.py：
# v = 1
# def f():
#     print("a function")
# class C:
#     def __init__(self):
#         self.a = 1

import importlib

module_name = "pkg.mod"
my_module = importlib.import_module(module_name)
print(my_module)    # <module 'pkg.mod' from 'xxx\\python_exercises\\_importlib\\pkg\\mod.py'>
print(my_module.v)  # 1
print(my_module.f)  # <function f at 0x000002205BB34310>
print(my_module.C)  # <class 'pkg.mod.C'>

# 导入方式
print(importlib.import_module("pkg.mod"))      # 绝对导入，类似于 import pkg.mod
print(importlib.import_module(".mod", "pkg"))  # 相对导入，类似于 from pkg import mod
# from pkg import mod
import pkg.mod
print(pkg.mod)

# 相对路径包导入（和动态导入这个主题无关，但是因为模块刚好在sibling_module外面，就顺便用上了
# import pkg2.sibling_pkg2.mod2    #详见mod2的内容
# print(pkg2.sibling_pkg2.mod2)
