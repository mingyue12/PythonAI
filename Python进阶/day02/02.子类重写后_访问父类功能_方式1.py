"""
案例：子类重写父类，继续访问父类功能
思路：
    1.父类名。父类函数名（self）   精准访问，想找哪个父类，就调哪个父类
    2.super().父类函数名（）   访问父类的函数，无需指定父类名，默认访问第一个父类
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

    # 调用父类的功能
    def make_master_cake(self):
        Master().__init__()
        Master().make_cake()

    def make_school_cake(self):
        School().__init__()
        School().make_cake()

# 测试
if __name__ == '__main__':
    # 创建徒弟类对象
    td = Prentice()
    # 访问属性
    print(td.kongfu)
    # 调用函数
    td.make_cake()
    td.make_master_cake()
    td.make_cake()
    td.make_school_cake()