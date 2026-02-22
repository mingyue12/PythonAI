"""
案例：继承入门

继承介绍：
    概述：
        子类可以继承父类的属性和方法
        子类可以重写父类的方法
    写法：
        class 子类名(父类名):
            pass
    例如:
        class A(B):
            pass
    叫法：
        A：子类，派生类
        B: 父类，基类，超类
    好处：
        提高代码的复用率
    弊端:
        增加了类之间的耦合度
    扩展：
        高内聚，低耦合
        内聚:
            类内部的属性和方法都紧密相关，互不干扰
        耦合:
            类之间的关系越紧密，耦合度越高
"""

# 需求：定义父类（男，散步），定义子类，继承父类
# 1.定义父类
class Father(object):
    def __init__(self):
        self.gender = '男'

    def walk(self):
        print("饭后走一走，活到九十九")

# 2.定义子类
class Son(Father):
    pass

# 3.测试子类
s = Son()
print(f"性别：{s.gender}")
s.walk()
