"""
案例：闭包入门

闭包解释：
    概述：
        使用了外部函数的变量的内部函数，就称之为闭包
    格式：
        def 外部函数(形参列表):
            外部函数的局部变量
            def 内部函数名(形参列表):
                使用外部函数的变量

            return 内部函数名

细节：
    1.函数名 和 函数名()是两个概念 前者表示函数对象，获取返回值

"""

# 案例一：函数名->是对象
def get_sum(a, b):
    return a + b

print(get_sum(1, 2))  # 3

# 函数名可以复制给变量，这个变量就是函数对象
my_func = get_sum
print(my_func)  # <function get_sum at 0x0000000000000000>
print(get_sum)  # <function get_sum at 0x0000000000000000>
print(my_func(1, 2))  # 3


