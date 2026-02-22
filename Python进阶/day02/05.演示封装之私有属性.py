"""
案例：演示封装之私有属性
封装简介：
    概述：
        属于面向对象的三大特征之一，就是隐藏对象的属性和实现细节，仅对外提供公用访问方式
    好处：
        1.提高代码的安全性  由属性的私有化实现
        2.提高代码的复用性  由函数来实现
    弊端：
        代码量增加，因为私有内容外界想访问，需要通过函数来实现
"""


# 演示
# 定义师傅类

# 定义学校类

# 定义徒弟类
class Prentice(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'
        self.__money = 200000

    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")


    # 针对私有属性，提供公有的访问方式
    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

# 定义徒孙类
class TuSun(Prentice):
    pass


# 测试
if __name__ == '__main__':
    ts = TuSun()
    print(ts.kongfu)
    print("-" * 34)
    print(ts.get_money())
    print("-" * 34)
    ts.set_money(100)
    print(ts.get_money())
