"""
案例：演示类方法和静态方法
类方法：
    属于类的方法，可以通过类名调用，也可以通过对象名调用
    定义：在方法上添加装饰器@classmethod
    第一个参数必须是cls，代表类本身
静态方法：
    属于类的方法，还可以通过对象名调用，只能通过类名调用
    定义：在方法上添加装饰器@staticmethod

区别：
    1.类方法前面的第一个参数是cls，代表类本身
    2.静态方法没有第一个参数
    3.你可以理解为函数中要用类对象，就定义成类方法，否则定义成静态方法
"""
# 定义学生类
class Student:
    # 2.定义类属性
    school = "黑马"

    # 3.定义类方法
    @classmethod
    def show1(cls):
        print(f'cls: {cls}')
        print(cls.school)
        print("我是类方法")

    # 4.定义静态方法
    @staticmethod
    def show2():
        print(Student.school)
        print("我是静态方法")


# 测试
if __name__ == '__main__':
    s1 = Student()
    s1.show1()
    print("-" * 34)
    s1.show2()
