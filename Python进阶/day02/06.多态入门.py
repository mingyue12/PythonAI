"""
案例：演示多态入门

多态概述：
    专业版：
        多态是指在不同的对象上调用相同的方法，会产生不同的行为。
        同一个函数，接收不同的参数，有不同的效果。
    前提条件：
        1.要有继承
        2.要有方法重写，不然多态无意义
        3.要有父类引用指向子类对象
    案例：
        动物类案例

"""


# 定义动物类

class Animal(object):  # 抽象类（也叫接口）
    def speak(self):  # 抽象方法
        pass


# 定义子类，狗类
class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


class Car:
    def speak(self):
        print("滴滴滴")


# 定义函数，接受不同的动物对象，调用speak方法
def make_noise(an:Animal):
    an.speak()


# 测试
if __name__ == '__main__':
    an:Animal = Dog() # 父类引用指向子类对象

    d = Dog()
    c = Cat()
    # 演示多态
    make_noise(d)
    make_noise(c)

    # 测试汽车类
    car = Car()
    make_noise(car) # Python是伪多态