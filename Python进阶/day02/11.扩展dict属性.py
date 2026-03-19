"""
该文件用于扩展dict属性
__dict__
属性：__dict__
说明：该属性用于存储对象的所有属性信息
可以把对象的所有属性信息转换为字典格式
"""
from 学生管理系统面向对象版.student import Student
# 需求：把学生类的所有属性信息转换为字典格式，属性名作为键，属性值作为值
s1 = Student("张三", "男", 18, "13800000000", "一个学生")
print(s1)

my_dict = s1.__dict__
print(my_dict)
print('-' * 30)

# 需求2：把[学生对象，学生对象，学生对象]转换为字典格式[{}, {}, {}]
s1 = Student("张三", "男", 18, "13800000000", "一个学生")
s2 = Student("李四", "男", 19, "13800000001", "一个学生")
s3 = Student("王五", "男", 20, "13800000002", "一个学生")
stu_list = [s1, s2, s3]
print(stu_list)

# 列表推导式
list_dict = [stu.__dict__ for stu in stu_list]

print(list_dict)

# 需求3：把{'name': '王五', 'sex': '男', 'age': 20, 'phone': '13800000002', 'desc': '一个学生'}转换为学生对象
my_dict = {'name': '王五', 'gender': '男', 'age': 20, 'phone': '13800000002', 'desc': '一个学生'}
s5 =Student(**my_dict)
print(s5)
