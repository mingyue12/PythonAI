
# 当使用变量时，初始化的值没有任何要求，可以用None代替
age = None

for i in range(5):
    age = int(input("您的年龄是？"))
    print("您的年龄是：", age)

print(f"最后一个同学的年龄是：{age}")
