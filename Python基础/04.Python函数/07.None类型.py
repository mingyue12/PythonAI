def say_hi():
    print("hi")


def say_hi2():
    print("啦啦啦")
    return None


x = say_hi()
print(x)  # 结果None，表示什么都没有
print(type(x))  # 类型NoneType，表示什么都没有类型

y = say_hi2()
print(y)  # 结果None，表示什么都没有
print(type(y))  # 类型NoneType，表示什么都没有类型
