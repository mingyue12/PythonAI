

def user_info(name, age, gender):
    print(f"我是{name}, 我今年{age}岁, 性别{gender}")


# 位置参数
user_info("张三", 18, "男")

# 关键字参数
user_info(age=18, name="张三", gender="男")

# 混合使用位置参数和关键字参数
# 位置参数必须在关键字参数之前
user_info("张三", age=18, gender="男")

