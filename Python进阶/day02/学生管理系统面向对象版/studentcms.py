"""
该文件用于完成学生管理系统的具体业务操作
增删改查，保存学生信息等。。。
"""

# 1.导入学生类
from student import Student

# 2.定义学生管理系统类
class StudentCMS:
    # 2.通过魔法方法初始化学生管理系统对象
    def __init__(self):
        # 创建空列表用于存储学生信息
        self.stu_list = list()  # 学生对象
