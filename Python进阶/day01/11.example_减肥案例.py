"""
案例：减肥
需求：
    当前体重是100kg，每当他跑步一次，体重会减少kg，吃一次，增加2kg.
"""


class Student:
    # init函数初始化
    def __init__(self, current_weight):
        self.current_weight = 100

    def run(self):
        print("跑步ing")
        self.current_weight -= 0.5

    def eat(self):
        print("吃ing")
        self.current_weight += 2

    def __str__(self):
        return f"当前体重是{self.current_weight}kg"

# 创建对象
if __name__ == '__main__':
    # 创建对象
    xm = Student(current_weight=100)
    # 跑步
    xm.run()
    # 吃喝
    xm.eat()
    # 当前体重
    print(xm)

