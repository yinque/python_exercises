import os

# 设置目录路径
directory = './'

# 列出目录中的文件和文件夹
items = os.listdir(directory)

# 打印文件和文件夹名称
for item in items:
    print(item)
