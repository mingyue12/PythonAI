"""
案例：演示通过self关键字实现类内访问函数
作用：用于区分不同对象
总结：类内访问函数时，需要通过self关键字来访问对象的属性和方法。
"""


# 定义汽车类
class Car:
    # 属性

    # 行为
    def run(self):
        print(f'{self}汽车在跑')

    def work(self):
        print(f'我是work函数没我的self值是：{self}')
        self.run() # 本类当前对象的引用


# 创建汽车对象
c1 = Car()
print(f"我是work函数，我的self值：{c1}")
c1.run()
print("-" * 34)
c1.work()

print("=" * 34)

# 再次创建汽车对象
c2 = Car()
print(f"我是work函数，我的self值：{c2}")
c2.run()
print("-" * 34)
c2.work()