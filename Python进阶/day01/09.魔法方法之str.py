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


class Car:
    # 有参的__init__()函数，参数值由：外部对象自行赋值
    def __init__(self, color, number):
        """
        该魔法方法用于属性初始化
        :param color: 车的颜色
        :param number: 车轮子的数量
        """
        self.color = color
        self.number = number

    def show(self):
        print(f"我是{self}，我是{self.color}的，我有{self.number}个轮胎")


    def __str__(self):
        return f"我的颜色是{self.color}我有几个轮子{self.number}"


# 创建对象
c1 = Car(color='绿色', number=4)
print(c1)
