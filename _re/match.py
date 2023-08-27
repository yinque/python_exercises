# re.match从字符串的开头开始尝试匹配模式，并返回一个匹配对象或 `None`。适用于从字符串的起始位置进行精确匹配。
import re

# 尝试从字符串的起始位置匹配正则表达式
match = re.match(r'\d+', '123 hello 456')   # match(pattern, string)
print(match)    # <re.Match object; span=(0, 3), match='123'>   匹配成功返回Match对象
print(re.match("pattern", "string"))   # None   匹配失败match返回none
if match:
    print('匹配成功')
    print(f'匹配的文本: {match.group()}')    # 匹配的文本: 123
    print(f'匹配的起始位置: {match.start()}')     # 匹配的起始位置: 0
    print(f'匹配的结束位置: {match.end()}')    # 匹配的结束位置: 3
    print(f'匹配的起始和结束位置元组: {match.span()}')  # 匹配的起始和结束位置元组: (0, 3)
else:
    print('没有匹配')
