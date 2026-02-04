"""
集合可以进行添加、删除、遍历等操作
"""

# 添加元素，使用add()方法
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set1.add(10)
print(set1)

# 删除元素，使用remove()方法
set1.remove(10)
print(set1)

# pop()方法随机删除一个元素
set1.pop()
print(set1)

# 清空集合
set1.clear()
print(set1)

# 两个集合的差集，使用difference()方法
# 差集：集合A中包含而集合B中不包含的元素
# 集合A - 集合B = 集合A中包含而集合B中不包含的元素
# 原集合不变
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set2.difference(set3))
print(set3.difference(set2))

# 2个集合的差集消除
# set2.difference_update(set3)
# 在set2中删除set3中包含的元素
# 结果：set2被修改，set3不变
set2.difference_update(set3)
print(set2)
print(set3)

# 两个集合的并集，使用union()方法
# 并集：集合A中包含的元素，集合B中包含的元素，集合A和集合B中都包含的元素
# 原集合不变
set4 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set5 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set4.union(set5))
print(set5.union(set4))

# 统计集合中的元素个数，使用len()方法, 集合中的元素是唯一的，不重复的
set6 = {1, 1, 2}
print(len(set6))

# 集合的遍历,只可用for循环
for i in set6:
    print(i)