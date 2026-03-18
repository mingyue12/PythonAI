"""
该文件用于完成学生管理系统的具体业务操作
增删改查，保存学生信息等。。。
"""

# 1.导入学生类
from student import Student


# 2.定义学生管理系统类
class StudentCMS(object):
    # 2.通过魔法方法初始化学生管理系统对象
    def __init__(self):
        # 2.1创建一个空列表，用于存储学生对象
        self.students = []

    def show_menu(self):
        print("*" * 23)
        print("学生管理系统V2.0")
        print("\t1.添加学生")
        print("\t2.删除学生")
        print("\t3.修改学生")
        print("\t4.查询学生")
        print("\t5.显示所有学生")
        print("\t0.退出系统")
        print("*" * 23)


if __name__ == '__main__':
    StudentCMS().show_menu()
