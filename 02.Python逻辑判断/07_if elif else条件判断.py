"""
if 条件:
    条件成立时执行的代码
elif 条件:
    条件成立时执行的代码
elif 条件:
    条件成立时执行的代码
elif 条件:
    条件成立时执行的代码
...
...
else:
    以上条件都不成立时执行的代码

"""

height = int(input("请输入你的身高："))
vip_level = int(input("请输入你的会员等级："))
day = int(input("请输入日期："))

# 如果身高小于120 免费，或者VIP级别大于3免费，或者今天1号免费，否则收费10元
# 可以将input语句直接写入条件判断中
# 如 if input("请输入你的身高：") < 120:
print("欢迎来到黑马动物园")
if height < 120:
    print("您的身高未超出120cm，可以免费游玩")
elif vip_level > 3:
    print("您的VIP等级大于3，可以免费游玩")
elif day == 1:
    print("今天是1号，可以免费游玩")
else:
    print("请付费游玩,票价十元")

