"""
案例：创建类的格式

格式1：
    class 类名:
        pass

格式2：
    class 类名():
        pass

格式3：
    # object是所有类的父类，所有类都默认继承object类
    class 类名(object):
        pass
"""
from pandas.core.array_algos.take import take_1d


# 需求定义一个老师类
# class Teacher:
#     pass
class Teacher(object):  # object是所有类的父类，所有类都默认继承object类
    pass


t1 = Teacher()
print(t1)