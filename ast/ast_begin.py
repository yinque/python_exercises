import ast

# 要分析的 Python 代码
source_code = """
def greet(name):
    print("Hello, " + name + "!")

greet("John")
"""

# 将源代码解析为抽象语法树（AST）
tree = ast.parse(source_code)

# 遍历 AST，打印函数定义和函数调用
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        print("Function Definition:", node.name)
    elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        print("Function Call:", node.func.id)
