# 作为被导入的模块
# 研究同级包的导入语法
from . import mod3
print(mod3)         # <module 'pkg2.mod3' from 'xxx\_base\\import_keyword\\pkg2\\mod3.py'>
from .mod3 import f3
print(f3)           # <function f3 at 0x0000020163029430>

# 总结：
# .访问符号代表该模块所属的包，而不是什么当前目录
# 直接运行该模块是错误的，会提示ImportError: attempted relative import with no known parent package
# 因为主模块不属于任何包
# 因此，该模块必须是被导入的，而且是带上包名导入的（反例见main2.py）
