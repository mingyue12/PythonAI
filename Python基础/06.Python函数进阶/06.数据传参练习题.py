def func1(name, age, *args, **kwargs):
    print(f"姓名：{name}")
    print(f"年龄：{age}")
    for i in args:
        print(i, end=" ")
    print()
    print("我的其他信息：")

    for key, value in kwargs.items():
        print(f"{key}: {value}")


func1("张三", 11, 1, 2, 3, 4, id=1001, na="张三", ag=11, sex="男")
