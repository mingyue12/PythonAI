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

    # 3.定义函数实现打印菜单
    @staticmethod
    def show_menu():
        print("*" * 23)
        print("学生管理系统V2.0")
        print("\t1.添加学生")
        print("\t2.删除学生")
        print("\t3.修改学生")
        print("\t4.查询单个学生信息")
        print("\t5.显示所有学生信息")
        print("\t6.保存学生信息")
        print("\t0.退出系统")
        print("*" * 23)
        print()

    # 4.定义函数，实现添加学生信息
    def add_student(self):
        pass

    # 5.定义函数实现删除学生信息、
    def del_student(self):
        pass

    # 6.定义函数，实现修改学生信息
    def update_student(self):
        pass

    # 7.定义函数，实现查询单个学生信息
    def query_student(self):
        pass

    # 8.定义函数，实现显示所有学生信息
    def show_all_students(self):
        pass

     # 9.定义函数，实现保存学生信息
    def save_students(self):
        pass

    # 10.定义函数，实现从文件中加载学生信息
    def load_students(self):
        pass

    # 11.定义函数，实现退出系统
    def exit_system(self):
        pass

    # 12.定义函数，实现系统主循环
    def start(self):
        # 11.1
        # 11.2 循环执行
        while True:
            # 11.3
            # 11.4 打印提示界面
            self.show_menu()
            # 11.5 获取用户输入
            input_num = input("请输入要操作的编号：")
            # 11.6 根据用户输入，调用不同的函数实现不同的操作
            if input_num == "1":
                # 添加学生信息
                print("添加学生信息\n")
                self.add_student()
            elif input_num == "2":
                # 删除学生信息
                print("删除学生信息\n")
                self.del_student()
            elif input_num == "3":
                # 修改学生信息
                print("修改学生信息\n")
                self.update_student()
            elif input_num == "4":
                # 查询单个学生信息
                print("查询单个学生信息\n")
                self.query_student()
            elif input_num == "5":
                # 显示所有学生信息
                print("显示所有学生信息\n")
                self.show_all_students()
            elif input_num == "6":
                # 保存学生信息
                print("保存学生信息\n")
                self.save_students()
            elif input_num == "0":
                # 退出系统做二次校验
                confirm = input("确定要退出系统吗？(y/n) ")
                if confirm.lower() == "y":  # 字符串.lower() 方法，将字符串中的所有大写字母转换为小写字母
                    print("退出系统")
                    break
                else:
                    continue
            else:
                print("输入有误，请重新输入")


if __name__ == '__main__':
    StudentCMS().start()
