import random
random_num = random.randint(1, 10)

# 第一次要求用户猜数字
num = int(input("请输入一个1-10之间的数字："))

if num == random_num:
    print("恭喜你，猜对了！")
else:
    if num > random_num:
        print("你猜大了")
    else:
        print("你猜小了")

    num = int(input("请输入一个1-10之间的数字："))

    if num == random_num:
        print("恭喜你，猜对了！")
