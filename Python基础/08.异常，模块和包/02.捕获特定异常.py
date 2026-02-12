"""
捕获特定异常
在Python中，可以使用try-except语句来捕获特定的异常类型。
当代码块中发生异常时，程序会跳转到对应的except块进行处理。
通过指定异常类型，可以更精确地捕获和处理不同类型的异常。
如果出现的异常不是指定的类型，程序会继续执行后续的代码并报错。
"""
try:
    1 / 0
except ZeroDivisionError as e:  # 捕获的是ZeroDivisionError异常
    print("不能除0")
    print(f"捕获到异常：{e}")
