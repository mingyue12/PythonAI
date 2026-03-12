"""
案例：演示抽象类的用法

抽象类解释：
    概述：
        在Python中，抽象类=接口，即：有抽象方法的类就是抽象类，也叫接口
        抽象方法 = 没有方法体的方法，即：方法体是pass修饰的
    作用/目的：
        抽象类一般充当父类，用于指定行业规范，准则，具体的实现交互由子类来完成实现
"""


class AC:
    # 1.1 制冷
    def cool_wind(self):
        pass

    # 1.2 制热
    def hot_wind(self):
        pass

    # 1.3 左右摆风
    def swing_wind(self):
        pass


# 2. 定义子类
class XiaoMi(AC):
    # 1.1 制冷
    def cool_wind(self):
        print("小米空调制冷")

    # 1.2 制热
    def hot_wind(self):
        print("小米空调制热")

    # 1.3 左右摆风
    def swing_wind(self):
        print("小米空调左右摆风")


class Gree(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_wind(self):
        print("格力空调左右摆风")

# 3. 测试
if __name__ == '__main__':
    # 场景1： 小米空调
    xm = XiaoMi()
    xm.cool_wind()
    xm.hot_wind()
    xm.swing_wind()
    print("-" * 34)
    # 场景2： 格力空调
    g = Gree()
    g.cool_wind()
    g.hot_wind()
    g.swing_wind()
