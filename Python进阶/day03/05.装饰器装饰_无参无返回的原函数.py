"""
案例：装饰器装饰_无参无返回的原函数
细节：
    装饰器的内部函数格式要和被装饰的原函数保持一致，
    即：原函数无参无返回，装饰器的内部函数也必须是无参无返回
"""

# 需求：定义无参无返回的get_sum()求和函数，在不改变其代码的基础上，添加友好提示，
# 定义装饰器
def tip(fu_name):
    def fuc_innder():
        # 添加提示信息（额外功能）
        print("努力计算中")
        # 调用原函数
        fu_name()
    # 返回内部函数
    return fuc_innder

# 定义原函数
@tip
def get_sum():
    a = 10
    b = 20
    sum = a + b
    print("和为：", sum)

get_sum()