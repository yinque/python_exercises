import os

FOLDER_PATH = 'learning_path'

os.chdir("./")  # 调整工作目录避免出现相对路径 FOLDER_PATH = './learning_path'时，root会出现./learning_path\sub1这种字符串


for root, dirs, files in os.walk('./'):
    print(f'当前文件夹：{root}')
    print(f'子文件夹列表：{dirs}')
    print(f'文件列表：{files}')
    print('----------------')
