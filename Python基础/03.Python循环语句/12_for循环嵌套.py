"""
需求：每天都去表白，共100天
每次：表白送10个花，说一句我喜欢你
"""

for i in range(1, 101):
    print("第%d天表白" % i)

    for j in range(1, 11):
        print("送%d朵花" % j)

    print("我喜欢你")
