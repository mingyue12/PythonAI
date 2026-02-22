"""
案例：演示多继承
需求：小明学习摊煎饼果子
扩展：MRO机制
    Pyhon中有MRO机制，可以查看某个对象，在调用函数时的顺序，即：先找哪个类，后找哪个类
    格式：
        类名.__mro__
"""
# 1.定义师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu}摊煎饼果子")

# 2.定义黑马学校类
class School():
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")
# 3.定义徒弟类，对象叫小明
class Prentice(School, Master): # 从左往右就近原则
    pass

# 测试
xm = Prentice()
xm.make_cake()
print("-" * 34)

# MRO机制
print(Prentice.mro())
print(Prentice.__mro__)
