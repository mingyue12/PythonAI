import time

s = time.time()

# open
f = open("hi.txt", "w", encoding="utf-8")

# 写入
for i in range(1000000):
    f.write("hello world\n")
    f.flush()

# 刷新
f.flush()

# 关闭
f.close()
# 输出运行所用时间
end = time.time()
print(end - s)
