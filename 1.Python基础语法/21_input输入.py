
print("你是谁？")
name = input("请告诉我你是谁？")
print("你的名字是：%s" % name)

# 无论输入什么都是字符串

var = input("请输入信息")
print(f"你输入的信息是：{var},类型是：{type(var)}")

# 输入年龄,注意类型转换
age = int(input("请输入年龄："))
