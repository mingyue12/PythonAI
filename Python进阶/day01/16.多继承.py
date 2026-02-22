"""
案例：演示多继承
需求：小明学习摊煎饼果子
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