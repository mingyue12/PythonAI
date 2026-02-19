"""
演示魔法方法__init__()
在创建对象的时候，会自动调用，一般用于该类对象的初始化操作
"""


# 需求：创建汽车类，不给默认值，由汽车对象外部赋值

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


# 创建汽车类对象
c1 = Car("red", 1)
c1.show()
print("-" * 50)
c2 = Car("blue", 2)
c2.show()