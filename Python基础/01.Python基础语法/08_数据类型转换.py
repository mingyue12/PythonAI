"""
    数据类型的转换
"""

# 数字转字符串，任何类型都可以 转字符串
t1 = str(123)
print(type(t1))
t2 = str(12.34)
print(type(t2))

# 整数和浮点数互转
print(float(123))
print(int(123.45))  # 浮点数转整数会丢失小数精度


# 字符串转数字,字符串必须是纯数字才可以强制转换
t3 = int("123")
t4 = float("123.65")
print(type(t3))
print(type(t4))
