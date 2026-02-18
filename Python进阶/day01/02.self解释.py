"""
案例： self关键字介绍

self介绍：
    概述：
        self是一个指向当前对象的引用，用于访问对象的属性和方法。
    作用：
        1. 访问对象的属性
        2. 调用对象的方法
        3. 谁调用函数self就指向哪个对象
"""


class car:
    # 属性

    # 行为
    def run(self):
        print("汽车会跑... ...")
        print(f"我是run函数，self的值是：{self}")


# 创建汽车对象
car1 = car()
print(f"car1：{car1}")
print(f"car1对象的地址值是：{id(car1)}")
print("-" * 34)
# 调用汽车对象的run方法
car1.run()

print()

car2 = car()
print(f"car2<UNK>{car2}")
print(f"car2<UNK>{id(car2)}")
print("-" * 34)
# 调用汽车对象的run方法
car2.run()