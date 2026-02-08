# 1.打开文件
# 2.读取文件内容
# 3.关闭文件

f = open("hi.txt", "r", encoding="utf-8")


for line in f:
    print(line.strip())

# 这个写法等同于
for line in f.readlines():
    print(line.strip())

# 方式2
for line in open("hi.txt", "r", encoding="utf-8"):
    print(line.strip())
 # OPEN打开文件，for循环读取行，for循环结束后会自动close文件

f.close()
