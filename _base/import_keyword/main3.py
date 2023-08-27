# 研究导入包的方法

# 导入的模块内容
# v = 1
# def f():
#     print("a function")
# class C:
#     def __init__(self):
#         self.a = 1

# 同级模块导入
import mod5
from mod5 import f
print(mod5)   # <module 'mod5' from 'xxx\\python_exercises\\_base\\import_keyword\\mod5.py'>
print(f)    # <function f at 0x000002765D43C0D0>

# 同级包内的模块导入
import pkg2.mod4    # import pkg.mod
print(pkg2)          # <module 'pkg2' (namespace)>
print(pkg2.mod4)      # <module 'pkg2.mod4' from 'xxx\\python_exercises\\_base\\import_keyword\\pkg2\\mod4.py'>
# print(mod4)  # name 'mod4' is not defined

del pkg2
# from pkg2 import mod4.v     #invalid
from pkg2.mod4 import v
print(v)    # 1
from pkg2 import mod4
print(mod4)         # <module xxx>
# print(pkg2)   name 'pkg2' is not defined

# 总结：
# 使用import pkg2.mod4语法时，会同时导入pkg2这个包的namespace和pkg2.mod4的变量
