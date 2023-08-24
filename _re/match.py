import re

pattern = r'\d+'  # 匹配一个或多个数字
string = '123 hello 456'

# 尝试从字符串的起始位置匹配正则表达式
match = re.match(pattern, string)

if match:
    print('匹配成功')
    matched_text = match.group()  # 获取匹配的文本
    start_position = match.start()  # 获取匹配的起始位置
    end_position = match.end()  # 获取匹配的结束位置
    span = match.span()  # 获取匹配的起始和结束位置的元组

    print(f'匹配的文本: {matched_text}')
    print(f'匹配的起始位置: {start_position}')
    print(f'匹配的结束位置: {end_position}')
    print(f'匹配的起始和结束位置: {span}')
else:
    print('没有匹配')