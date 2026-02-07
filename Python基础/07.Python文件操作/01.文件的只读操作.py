"""
文件操作3大步
1.打开文件
2.操作文件
3.关闭文件
"""

# 打开文件
# 绝对路径写法
# f1 = open("D:\\hi.txt", "r", encoding="utf-8")
# 相对路径写法
# 相对路径写法，注意当前的工作目录，在脚本所在目录寻找
f2 = open("hi.txt", "r", encoding="utf-8")
# print(f2.read())


# read([size])方法读取文件内容
# 1.不传入size参数，默认读取整个文件内容
# ontent = f2.read("D:\\hi.txt", "r", encoding="utf-8")
# print(content)

content = f2.read(30)
print(content)

# readlines()方法读取文件内容，返回一个列表，每个元素是文件的一行内容
lines = f2.readlines()
print(lines)
print(len(lines))
for i in lines:
    # readlines每一行的换行\n不会清除
    # 可以使用lines = lines.strip("\n")清除换行符
    print(i)

# readline()方法读取文件内容，返回一个字符串，每次读取一行内容
# 重复调用readline()方法，每次读取一行内容
line = f2.readline()
print(line)


# 关闭文件
f2.close()
