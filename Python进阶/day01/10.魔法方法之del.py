"""
案例：演示init魔法方法的用法
魔法方法：
    概述：
        Python内置函数，满足特定条件自动触发
        常用魔法方法：
            __init__()  # 在创建对象的时候，会自动触发该类的__init__()函数
            __str__()  # 在使用print()函数打印对象时，会自动触发该类的__str__()函数
            __del__()  # 在删除对象时，会自动触发该类的__del__()函数
"""


# 1.定义汽车类，属性：品牌，行为run，通过del魔法方法删除该类的对象
class Car:
    # init函数初始化
    def __init__(self, brand):
        self.brand = brand

    # 重写__str__()函数
    def __str__(self):
        return f"我是{self.brand}汽车"

    # 重写__del__()函数
    def __del__(self):
        print(f"{self.brand}汽车被删除了")


# 创建对象
c1 = Car(brand="小米 su7 Ultra")
print(c1)

# 手动访问brand属性
print(c1.brand)
print('-' * 34)

# 手动删除对象，并尝试打印对象
del c1
