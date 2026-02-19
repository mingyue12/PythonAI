"""
案例：演示init魔法方法的用法
魔法方法：
    概述：
        Python内置函数，满足特定条件自动触发
        常用魔法方法：
            __init__()  # 在创建对象的时候，会自动触发该类的__init__()函数
            __str__()  #
            __del__()  #
"""


# 需求：定义汽车类，默认属性为：color = '黑色'，number = 3
# 1.定义汽车类
class Car:
    # 1.1 在魔法方法__init__()中初始化属性
    def __init__(self):
        # 1.1.1 初始化属性
        print("init初始化函数")
        # 1.1.2 初始化属性
        self.color = '黑色'
        self.number = 4

    def show(self):
        print(f"我是{self}，我是{self.color}的，我有{self.number}个轮胎")


# 创建汽车类对象
print("-" * 34)
c1 = Car()  # 会自动调用__init__()函数
# 修改属性
c1.color = '红色'
c1.number = 6
print(c1.color, c1.number)
c1.show()
print("-" * 34)
c2 = Car()
c2.show()
