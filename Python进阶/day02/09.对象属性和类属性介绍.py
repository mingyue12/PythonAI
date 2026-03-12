"""
案例：对象属性和类属性介绍

属性介绍:
    概述：
        用来描述事物的外在特征
    分类：
        1. 对象属性：
            概述：
                每个对象都有自己的属性，即：对象属性是对象特有的属性
            定义：
                在类的方法中，使用self.属性名 = 属性值的方式定义对象属性
        2. 类属性：
            概述：
                所有对象都共享的属性，即：类属性是类共有的属性
            定义：
                在类中，方法外定义的属性，即：属性名 = 属性值的方式定义类属性
"""
# 需求：演示对象属性和类属性相关
# 1.定义一个Student类每个学生都有自己的姓名和年龄
class Student:
    # 1.1 定义类属性
    teacher_name = "王老师"
    # 1.2 定义对象属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义str魔法方法，输出对象的信息
    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}"

# 测试
if __name__ == '__main__':
    s1 = Student("张三", 18)
    s1.name = "王五"
    s2 = Student("李四", 18)
    print(s1)
    print(s2)
    print("-" * 34)
    # 场景2：类属性
    # 类属性可以通过类名访问，还可以通过对象名访问
    print(s1.teacher_name)
    print(Student.teacher_name)

    s1.teacher_name = "测试"
    print(s1.teacher_name)
    print(s2.teacher_name)
    print(Student.teacher_name)

    Student.teacher_name = "<UNK>"
    print(s1.teacher_name)
    print(s2.teacher_name)
    print(Student.teacher_name)