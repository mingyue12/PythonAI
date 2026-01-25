
# for循环中定义的变量，在循环外是无法使用的，但是不强制要求
# 如需访问临时变量，需先在外定义它
age = 0
num = 10
for i in range(5):
    age = 19
    print(num)

print(age)
