
# 只有三次猜测机会
# 猜对了，打印恭喜，并退出程序
# 猜错了，打印猜错了，请重新输入

num = 10
if int(input("请输入一个数字：")) == num:
    print("恭喜你，猜对了")
elif int(input("猜错了请继续输入：")) == num:
    print("恭喜你，猜对了")
elif int(input("猜错了请继续输入：")) == num:
    print("恭喜你，猜对了")
else:
    print("很遗憾，你没有猜对")
