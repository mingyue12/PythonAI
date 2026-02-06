
# 元组的不可修改特性演示
# 创建一个元组
my_tuple = (1, 2, 3, 4, 5)
print("原始元组:", my_tuple)
# 尝试修改元组中的元素
try:
    my_tuple[0] = 100
except TypeError as e:
    print("修改元组元素时出错:", e)


# 元组中的列表元素
# 元组中的元素可以是列表，列表是可变的，所以元组中的列表元素是可以修改的
my_tuple1 = (1, 2, [3, 4, 5])
print("原始元组:", my_tuple)
# 尝试修改元组中的列表元素
try:
    my_tuple1[2][0] = 100
except TypeError as e:
    print("修改元组中的列表元素时出错:", e)
print("修改后的元组:", my_tuple1)


for i in my_tuple1:
    print(i)