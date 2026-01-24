"""
需求：每天都去表白总计100天
每次：表白送10个花说一句我喜欢你
"""
day = 1
while day <= 100:
    print("第%d天，我喜欢你" % day)
    counter = 1    # 内层循环控制因子
    while counter <= 10:
        print("送小美的第%d朵花" % counter)
        counter += 1
    print("我喜欢你")
    day += 1
