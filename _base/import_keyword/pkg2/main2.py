# 作为主模块运行

import mod2     # 错误的，提示ImportError: attempted relative import with no known parent package

# 总结
# 主模块中使用不带包名的import语句导入一个“代码中含有.包访问符号”的包会报错