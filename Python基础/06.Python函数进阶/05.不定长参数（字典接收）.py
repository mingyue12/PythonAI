
def func(name, **kwargs):
    """
    **kwargs是不定长参数的标记，表示接收任意数量的关键字参数，封装成字典
    """
    print(f"我们是：{name}，我们的成员有：")
    print(kwargs)


func("aa", id = 1001, na = "张三", age = 11, sex = "男")

def func2(name, age, *args, **kwargs):
    print(f"元组收集: {args}")
    print(f"字典收集: {kwargs}")

# 正确调用
func2("周杰伦", 11, 1, 2, 3, 4, id=1, na=2, gender="男")
