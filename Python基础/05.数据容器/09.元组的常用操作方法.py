t1 = (1, 2, 3, "a", "b", "c")
# 元组的常用操作方法

# index() 方法
# 用于查找指定元素在元组中的索引位置。如果元素不存在，会抛出 ValueError 异常。
print(t1.index("a"))  # 输出: 3
print(t1.index(2))  # 输出: 1
# print(t1.index("z"))  # ValueError: tuple.index(x): x not in tuple


t1 = (1, 2, 3, "a", "b", "c")
# count() 方法
# 用于统计元组中指定元素的出现次数。
print(t1.count(1))  # 输出: 1
print(t1.count("a"))  # 输出: 1
print(t1.count("z"))  # 输出: 0
