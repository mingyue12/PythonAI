"""
案例：装饰器装饰_无参无返回的原函数
细节：
    装饰器的内部函数格式要和被装饰的原函数保持一致，
    即：原函数无参无返回，装饰器的内部函数也必须是无参无返回
"""

# 需求：定义有参无返回的get_sum()求和函数，在不改变其代码的基础上，添加友好提示，
# 装饰器内部函数，要和被装饰函数保持一致
# 定义装饰器
def my_decorator(func_name):
    # 定义内部函数
    def func_inner():
        # 添加提示信息（额外功能）
        print("正在计算")
        # 调用原函数
        return func_name()
    return func_inner



# 定义原函数,有参无返回值
@my_decorator
def get_sum():
    a = 11
    b = 22
    return a + b


flag = get_sum()
print(flag)