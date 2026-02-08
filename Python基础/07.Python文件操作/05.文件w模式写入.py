"""
mode:
w: 写入模式
        如果文件不存在，会创建文件
        如果文件存在，会清空文件内容
a: 追加模式
r: 读取模式
"""

# 打开
f = open("hi.txt", "w", encoding="utf-8")

# 将helloworld写入文件
# 写入内容后，文件指针会移动到文件末尾
# 将文件内容写入缓冲区
f.write("helloworld")
# f.flush()
# 刷新缓冲区，将文件内容写入文件
f.flush()

# 关闭
f.close()
