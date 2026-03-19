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
        # 4.1 提示用户输入学生信息，并接受
        name = input("请输入姓名：")
        gender = input("请输入性别：")
        age = int(input("请输入年龄："))
        phone = input("请输入手机号：")
        desc = input("请输入信息：")
        # 4.2 创建学生对象
        stu = Student(name, gender, age, phone, desc)
        # 4.3 将学生对象添加到列表中
        self.students.append(stu)
        # 4.4 打印添加成功信息
        print("添加成功！\n")
        print(stu)

    # 5.定义函数实现删除学生信息、
    def del_student(self):
        # 5.1 提示用户输入要删除的学生姓名并接收
        del_name = input("请输入要删除的学生姓名：")
        # 5.2 遍历学生列表，判断是否有要删除的学生
        for stu in self.students:
            # 5.3 遍历学生列表，判断是否有要删除的学生
            if stu.name == del_name:
                self.students.remove(stu)
                print(f"{stu.name}的删除成功！\n")
                break
        else:
            print("要删除的学生不存在！\n")

    # 6.定义函数，实现修改学生信息
    def update_student(self):
        # 6.1 提示用户输入要修改的学生姓名并接收
        update_name = input("请输入要修改的学生姓名：")
        # 6.2 遍历学生列表，判断是否有要修改的学生
        for stu in self.students:
            # 6.3 遍历学生列表，判断是否有要修改的学生
            if stu.name == update_name:
                # 6.4.1 提示用户输入要修改的属性
                update_attr = input("请输入要修改的属性：")
                # 6.4.2 提示用户输入要修改的属性值
                update_value = input("请输入要修改的属性值：")
                # 6.4.3 修改学生属性
                # self.students.remove(stu)
                setattr(stu, update_attr, update_value)
                # self.students.append(stu)
                print(f"{stu.name}的{update_attr}已修改为{update_value}\n")
                # 6.4.2 打印修改成功信息
                print(f"{stu.name}的修改成功！\n")
                break
        else:
            print("要修改的学生不存在！\n")

    # 7.定义函数，实现查询单个学生信息
    def query_student(self):
        # 7.1 提示用户输入要查询的学生姓名并接收
        query_name = input("请输入要查询的学生姓名：")
        for stu in self.students:
            if stu.name == query_name:
                print(stu, end="\n")
                break
        else:
            print("要查询的学生不存在！\n")

    # 8.定义函数，实现显示所有学生信息
    def show_all_students(self):
        # 8.1 判断学生列表是否为空
        if len(self.students) == 0:
            print("当前没有学生信息！\n")
            return
        else:
            # 8.2 不为空遍历学生列表，打印所有学生信息
            for stu in self.students:
                print(stu)
            print()

    # 9.定义函数，实现保存学生信息
    def save_students(self):
        with open('stu_data.txt', 'w', encoding='utf-8') as f:
            # 9.2 把[学生对象，学生对象，学生对象]转换为字典格式[{}, {}, {}]
            stu_dict = [stu.__dict__ for stu in self.students]  # 列表推导式
            f.write(str(stu_dict))  # 记得转成字符串再存储
            print("保存成功！\n")

    # 10.定义函数，实现从文件中加载学生信息
    def load_students(self):
        # 10.1 加入异常处理
        try:
        # 10.2 关联学生信息文件
            with open('stu_data.txt', 'r', encoding='utf-8') as f:
                # 10.3 从文件中读取学生信息
                stu_dict = f.read()
                # 10.4 把字符串转换为列表
                stu_dict = eval(stu_dict)   # 字符串转列表
                # 10.5 判断列表是否为空
                if len(stu_dict) == 0:
                    self.students = []
                # 10.6 把列表中的字典转换为学生对象
                self.students = [Student(**stu_dict) for stu_dict in stu_dict]
        except FileNotFoundError:
            # 10.7 如果文件不存在，创建文件
            with open('stu_data.txt', 'w', encoding='utf-8') as f:
                pass

    # 11.定义函数，实现退出系统
    def exit_system(self):
        pass

    # 12.定义函数，实现系统主循环
    def start(self):
        # 11.1 加载学生信息
        self.load_students()
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
                self.save_students()
                print("保存学生信息\n")
            elif input_num == "0":
                # 退出系统做二次校验
                confirm = input("确定要退出系统吗？(y/n) ")
                if confirm.lower() == "y":  # 字符串.lower() 方法，将字符串中的所有大写字母转换为小写字母
                    self.save_students()
                    print("退出系统")
                    break
                else:
                    continue
            else:
                print("输入有误，请重新输入")


if __name__ == '__main__':
    StudentCMS().start()
    import os
    print(os.getcwd())
