# 作为主模块运行
# 测试.导入与..导入
# mod1.py
# from .. import mod4
# print(mod4)   <module 'pkg1.mod4' from 'xxx\\python_exercises\\_base\\import_keyword\\pkg1\\mod4.py'>
import pkg1.subpkg.mod1
print(pkg1.subpkg.mod1)     # <module 'pkg1.subpkg.mod1' from 'xxx\\python_exercises\\_base\\import_keyword\\pkg1\\subpkg\\mod1.py'>


import pkg2.mod2
print(pkg2.mod2)    #<module 'pkg2.mod2' from 'xxx\\python_exercises\\_base\\import_keyword\\pkg2\\mod2.py'>

# 总结:
# .代表该模块所属的包
# ..代表该模块所属的包的父包
# 无论是.还是..都需要导入它们的模块已经创建了包的namespace（namespace在使用import pkg.mod会自动创建一个pkg的namespace）