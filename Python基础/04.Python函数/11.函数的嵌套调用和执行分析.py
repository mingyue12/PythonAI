"""
函数的嵌套调用和执行分析
嵌套调用的基本原则是：先调用的函数先执行，后调用的函数后执行。
"""


def func_a():
    print("11111")


def func_b():
    print("22222")

    func_a()

    print("33333")


def func_c():
    print("44444")

    func_b()

    print("55555")


func_c()
