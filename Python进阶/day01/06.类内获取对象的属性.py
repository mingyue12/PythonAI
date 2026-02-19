"""
案例：类内获取对象的属性
"""


# 定义类
class Car:
    # 属性

    # 行为
    # 1.1跑
    def run(self):
        print("汽车在跑...")

    # 1.2定义函数show(),实现类内访问汽车对象的属性
    def show(self):
        print(f"我是show函数，对象的颜色是{self.color}，轮胎数是{self.num}")

# 2.创建汽车类的对象
c1 = Car()
# 3.给其设置属性
c1.color = "黄色"
c1.num = 4

# 4.类外访问属性
print(f"颜色{c1.color}，轮胎数{c1.num}")

# 5.类外访问行为
c1.run()
c1.show()