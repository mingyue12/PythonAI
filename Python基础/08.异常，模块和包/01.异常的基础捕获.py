f = None
try:
    # 感觉这里可能出现问题
    f = open("D:/test.txt", "r", encoding="utf-8")
except:
    # 如果出现问题，就会执行这里的代码
    f = open("D:/test.txt", "w", encoding="utf-8")

# 写模式下文件不可读
print(f.read())
f.close()
