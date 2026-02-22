"""
案例：子类重写父类功能
重写解释：
    概述：
        重写也叫覆盖，即：子类出现和父类重名的属性或者行为称之为重写。
    调用层次：
        当子类对象调用重写的属性或者行为时，会调用子类的属性或者行为。
        当子类对象调用未重写的属性或者行为时，会调用父类的属性或者行为。
        遵循就近原则，就近父类调用，依次向上查找。
"""

# 需求：
# 1.老师父类
class Master:
    # 1.1 属性
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    # 1.2 行为
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")

# 黑马学校类
class School:
    # 1.1 属性
    def __init__(self):
        self.kongfu = '黑马AI煎饼果子配方'

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

# 测试
if __name__ == '__main__':
    # 创建徒弟类对象
    td = Prentice()
    # 访问属性
    print(td.kongfu)
    # 调用函数
    td.make_cake()
