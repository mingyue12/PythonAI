
flag = 0
num = int(input("请输入一个整数："))
for x in range(1, num):
    if x % 2 == 0:
        flag += 1

print("1-%d偶数的个数为%d\n(不包含%d本身)" % (num, flag, num))
