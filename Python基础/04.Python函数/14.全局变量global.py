"""
全局变量：不定义在函数内部的变量就是全局变量，可以在函数内部使用，但不能在函数内部修改。
"""

num = 100  # 全局变量,作用域为全局。


def func_a():
    print("函数func_a内部：", num)  # 可以访问全局变量


def func_b():
    global num  # 声明使用全局变量num
    num = 200   # 修改全局变量num的值
    print("函数func_b内部：", num)  # 可以访问全局变量


func_a()
func_b()

print("函数外部：", num)  # 可以访问全局变量
