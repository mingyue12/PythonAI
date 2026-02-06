# 缺省参数（默认参数）,不传参则使用默认参数
# 默认值参数要求必须全部在右侧
def user_info(name, age, gender="男"):
    print(f"我是{name}, 我今年{age}岁, 性别{gender}")


user_info("张三", 18)
user_info("李四", 20, "女")


# 例如end是有默认值，默认值是换行符"\n"
print("hello world")

