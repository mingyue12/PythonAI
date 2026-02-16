# __all__ 内置Python变量列表用于指定模块中哪些名称可以被导入
# 默认是* 表示所有名称都可以被导入
# __all__ = ["say_hi", "say_hi2"] 表示只有say_hi和say_hi2可以被导入
# 只能控制import* 导入的名称，不能控制import 导入的名称


def say_hi():
    print("hi")


def say_hi2():
    print("hi2")


def say_hi3():
    print("hi3")
    print("hi3")
