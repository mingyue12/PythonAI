"""
该文件用于记录学生类，学生的属性信息为：姓名，性别，年龄，手机号，描述信息
"""


# 1.定义学生类
class Student:
    # 2.定义魔法方法，初始化属性信息
    def __init__(self, name, gender, age, phone, desc):
        """
        该魔法方法用于初始化学生信息
        :param name:    学生姓名
        :param gender:  学生性别
        :param age:     学生年龄
        :param phone:   学生电话
        :param desc:    学生信息
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.desc = desc

    # 3.定义魔法方法，用于打印学生信息
    def __str__(self):
        """
        该魔法方法用于打印学生信息
        :param return:  返回学生信息
        """
        return f"姓名：{self.name}，性别：{self.gender}，年龄：{self.age}，电话：{self.phone}，信息：{self.desc}"

if __name__ == '__main__':

    # 4.测试
    s = Student("张三", "男", 18, "13800000000", "一个学生")
    print(s)
