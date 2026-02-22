"""
案例：演示单继承，即1个子类继承自一个父类
分析：
    1.定义师傅类，Master
        属性：kongfu
        行为：make_cake()
    2.定义子类，Prentice，继承师傅类
"""

# 1.定义师傅类
class Master:
    def __init__(self):
        self.kongfu = '古法配方，摊煎饼果子'
    # 定义行为
    def make_cake(self):
        print(f"采用{self.kongfu}，做煎饼果子")


# 定义子类，Prentice，继承师傅类
class Prentice(Master):
    pass

# 3.测试子类
p = Prentice()
p.make_cake()
