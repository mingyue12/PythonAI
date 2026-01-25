"""
有十碗饭，挨个吃，吃之前问你饱没饱，吃饱了就不吃了
"""

for i in range(1, 11):
    flag = int(input(f"第{i}碗饭吃不吃，请输入是否吃饱了，1表示没吃饱，0表示吃饱了："))
    if flag == 0:
        break   # break会直接结束循环

    print(f"正在吃第{i}碗饭")
