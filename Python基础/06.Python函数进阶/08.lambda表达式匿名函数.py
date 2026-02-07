
def func(compute):
    # 调用compute函数
    result = compute(1, 2)
    print(result)

# lambda函数仅使用一次，不做重复使用，所以使用lanbda函数实现
func(lambda x, y: x + y)


# 重复利用写法，lambda函数可以赋值给一个变量，后续可以重复利用
chengfa = lambda x, y: x * y
print(chengfa(2, 3))