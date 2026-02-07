"""
- 形式参数，可以接收函数传入
- 实际参数，真的可以传入一个函数
- 函数作为参数传递，函数名不带括号
- 传入的是计算逻辑，调用时才执行
"""

def func(compute):
    # 调用compute函数
    result = compute(1, 2)
    print(result)


def compute(x, y):
    return x + y


# 传入compute函数作为参数
func(compute)
