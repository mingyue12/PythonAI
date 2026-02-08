"""
with open() as f:
    ...

以这种语法写，不需要手动close文件，会自动close文件
"""

with open("hi.txt", "r", encoding="utf-8") as f:
    f.readlines()
    for line in f:
        print(line.strip())
    # 不需要写close，会自动close文件