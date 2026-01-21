
age = int(input("请输入年龄："))
year = int(input("请输入入职时间："))
level = int(input("请输入工作级别："))
if age >= 18:
    if age > 30:
        if year >= 2:
            print("入职时间满两年，发礼物")
        elif level > 3:
            print("工作级别高，发礼物")
        else:
            print("年龄和工作级别都不符合要求,无礼物")
    else:
        print("年龄不符合要求")
else:
    print("年龄不符合要求")
