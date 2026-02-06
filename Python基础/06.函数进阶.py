

def func():
    # 返回了一个元组(1, 2)
    return 1, 2

# 自动解包，将元组的两个元素分别赋值给x和y
x, y = func()
print(x)
print(y)

# 只用一个变量可接受完整的元组
x = func()
print(x, type(x)) # (1, 2) <class 'tuple'>