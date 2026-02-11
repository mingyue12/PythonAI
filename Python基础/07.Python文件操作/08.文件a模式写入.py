"""
文件a模式写入
a模式：追加写入，如果文件不存在会创建，如果文件存在则在文件末尾继续写入，不会覆盖原有内容
w模式：写入模式
        如果文件不存在，会创建文件
        如果文件存在，会清空文件内容
"""


# open
f = open("hi.txt", "a", encoding="utf-8")

# write, 写入内容后，文件指针会移动到文件末尾
# write写入后不会自带换行
f.write("追加内容\n")

# flush
f.flush()

# close
f.close()