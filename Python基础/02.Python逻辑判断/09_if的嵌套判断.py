

# 需求：身高大于120需判断VIP级别大于3可以免费，身高小于120直接免费

if int(input("请输入身高：")) > 120:
    print("需要判断VIP级别")
    if int(input("请输入VIP级别：")) > 3:
        print("免费")
    else:
        print("付费")
else:
    print("免费")
