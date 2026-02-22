"""
案例：演示多重继承
多重继承介绍：
    类A继承类B，类B继承类B
继承体系：
    object -> Master -> School -> Prentice -> td
"""


# 需求：
# 1.老师父类
class Master:
    # 1.1 属性
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    # 1.2 行为
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")


# 黑马学校类
class School:
    # 1.1 属性
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    # 1.2 行为
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")


# 徒弟类
class Prentice(School, Master):
    def __init__(self):
        super().__init__()
        self.kongfu = '[独创煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")

    # 调用父类的功能
    def make_master_cake(self):
        Master().__init__()
        Master().make_cake()

    def make_school_cake(self):
        School().__init__()
        School().make_cake()


# 创建徒孙类
class TuSun(Prentice):
    pass

# 测试
if __name__ == '__main__':
    # 创建徒孙类对象
    ts = TuSun()
    # 调用行为
    ts.make_cake()
    ts.make_master_cake()
    ts.make_school_cake()