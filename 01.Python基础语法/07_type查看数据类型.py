"""
    通过type语句查看数据类型
    变量无类型存储的数据有类型
"""

# 语法： type(被查看的)  被查看的可以是: 字面量，变量
print(type(666))  # 整型
print(type(12.345))  # 浮点型
print(type("Hello World"))  # 字符串

# 存储类型信息

int_type = type(666)

# 输出
print(int_type)
