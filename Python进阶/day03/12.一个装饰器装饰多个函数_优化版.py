"""
案例：演示带参数的装饰器

记忆：1.一个转十七的参数有且只能有一个
     2.如果装饰器有多个函数，可以在该装饰器的外部再嵌套一层，
     把该装饰器当做其内部函数返回
"""
#  需求：定义一个既能装饰减法，又能装饰加法的装饰器 -> 即：带有参数的装饰器
# 1.定义装饰器

# 优化版
# def my_decorator(fn_name):    # fn_name:原函数名 flag:标记 报错，装饰器的参数只能有一个
#     # 定义内部函数格式和原函数保持一致
#     def fn_inner(a, b):
#         # 增加额外功能
#         if fn_name.__name__ == 'get_sum':
#             print("正在计算加法")
#         elif fn_name.__name__ == 'get_sub':
#             print("正在计算减法")
#         # 返回
#         return fn_name(a, b)
#     return fn_inner

# 标准版
def my_decorator(fn_name):
    def fn_inner(a, b):
        # 额外功能
        if fn_name.__name__ == 'get_sum':
            print("正在计算加法")
        elif fn_name.__name__ == 'get_sub':
            print("正在计算减法")
        # 返回
        return fn_name(a, b)
    return fn_inner

# 2.定义原函数，表示加法
@my_decorator
def get_sum(a, b):
    return a + b

# 3.定义原函数，表示减法
@my_decorator
def get_sub(a, b):
    return a - b


# 测试
print(get_sum(10, 20))
print('-' * 20)

print(get_sub(10, 20))

