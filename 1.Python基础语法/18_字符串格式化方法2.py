"""
    使用f_format方法进行格式化(快速格式化)
    1.字符串之前写f标记
    2.变量使用{}包起来
"""

name = "周杰伦"
age = 11
height = 172.55

message = "我是name，今年age岁，身高height厘米"
message2 = f"我是{name}，今年{age}岁，身高{height}厘米"
print(message)
print(message2)

