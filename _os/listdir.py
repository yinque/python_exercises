import os

# 设置目录路径
directory = './'

# 列出目录中的文件和文件夹
items = os.listdir(directory)

# 打印文件和文件夹名称
print("====file and dir list====")
for item in items:
    print(item)

file_items = [i for i in items if os.path.isfile(i)]
print("====file list====")
for item in file_items:
    print(item)
