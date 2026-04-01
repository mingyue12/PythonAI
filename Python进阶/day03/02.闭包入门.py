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
    前提条件：
        1.有嵌套函数 外部函数嵌套内部函数
        2.有引用 内部函数引用了外部函数的变量
        3.有返回值 外部函数中，返回内部函数（对象）
    注意：
        1.闭包的使用场景：
            1.需要在函数内部使用外部函数的变量
            2.需要在函数外部使用内部函数的变量
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

# 案例2：演示闭包写法
# 需求：定义求和的闭包，外部函数有参数num1，内部函数有num2调用，求解两数之和

# 1.定义外部函数
def fun_outer(num1):
    def fun_inner(num2):
        # 3.求解求和
        sum1 = num1 + num2
        print(f"求和结果",sum1)
    return fun_inner
# 4.调用上述函数
fun_inner = fun_outer(10)
fun_inner(1)    # 11
fun_inner(1)    # 11
fun_inner(1)    # 11





print('-' * 20)
fun_outer(100)(200)

