"""
案例：装饰器装饰_有参有有返回值的可变参数

细节：
    1. 装饰器内部的函数格式要和备装饰的原函数保持一致
   """


# 需求：定义1个可以计算多个数据和字典value值和的函数，并给其友好提示
# 1.定义装饰器
def my_decorator(func_name):
    # 定义内部函数
    def func_inner(*args, **kwargs):
        # 添加提示信息（额外功能）
        print("正在计算")
        # 调用原函数
        return func_name(*args, **kwargs)
    return func_inner

# 2.定义被装饰的函数
@my_decorator
def get_sum(*args, **kwargs):
    """
    该函数用于计算多个数据和字典value值的和
    :param args: 数字列表，*args接收所有的位置参数，封转到元组中
    :param kwargs: 字典，**kwargs接收所有的关键字参数，封转到字典中
    :return: 计算结果
    """
    # # 2.1 定义求和变量
    # sum = 0
    # # 2.2 遍历元组，获取每个元素，求和
    # for i in args:
    #     sum += i
    # # 2.3 遍历字典，获取每个元素，求和
    # for v in kwargs.values():
    #     sum += v
    #
    # # 2.4 返回求和结果
    # return sum
    return sum(args) + sum(kwargs.values())


# 3.测试
sum = get_sum(1, 2, 3, a=6, b=4, c=5)
print(sum)  # 18

# my_dict = {"a": 1, "b": 2, "c": 3}
#
# sum2 = sum(my_dict.values())
# print(sum2)  # 6
