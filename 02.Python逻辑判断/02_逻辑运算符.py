
"""
    逻辑运算符
    and: 与 多条件同时满足为True，否则False
    or: 或 多条件满足一个为True，则True，否则False
    not: 非 取反
"""

age = 19
print("5 < age < 18 = ? %s" % (age > 5 and age < 18))
print("5 < age 或 age < 18 = ? %s" % (age > 5 or age < 18))
print("age 是不是成年人 %s" % (not age < 18))
