"""
该文件用于程序的入口文件
"""
from studentcms import StudentCMS

# 程序的主入口
if __name__ == '__main__':
    stu_cms = StudentCMS()
    # 调用系统主循环
    stu_cms.start()
