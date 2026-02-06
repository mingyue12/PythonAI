
# 通用操作：遍历
# 遍历：for 变量 in 容器：
# 通用操作：求元素个数
# 求元素个数：len(容器)

# 找出最大值
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
s_str = "itheima"
s_set = {1, 3, 5, 7}
d = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

print(f"lst的最大值是：{max(lst)}")
print(f"t的最大值是：{max(t)}")
print(f"s_str的最大值是：{max(s_str)}")
print(f"s_set的最大值是：{max(s_set)}")
print(f"d的最大值是：{max(d)}") # 字典找的是key

# 找出最小值
print(f"lst的最小值是：{min(lst)}")
print(f"t的最小值是：{min(t)}")
print(f"s_str的最小值是：{min(s_str)}")
print(f"s_set的最小值是：{min(s_set)}")
print(f"d的最小值是：{min(d)}") # 字典找的是key

# 转列表
print(f"lst转列表是：{list(lst)}")
print(f"t转列表是：{list(t)}")
print(f"s_str转列表是：{list(s_str)}")
print(f"s_set转列表是：{list(s_set)}")
print(f"d转列表是：{list(d)}") # 字典转列表是key

# 转元组
print(f"lst转元组是：{tuple(lst)}")
print(f"t转元组是：{tuple(t)}")
print(f"s_str转元组是：{tuple(s_str)}")
print(f"s_set转元组是：{tuple(s_set)}")
print(f"d转元组是：{tuple(d)}") # 字典转元组是key

# 转集合
print(f"lst转集合是：{set(lst)}")
print(f"t转集合是：{set(t)}")
print(f"s_str转集合是：{set(s_str)}")
print(f"s_set转集合是：{set(s_set)}")
print(f"d转集合是：{set(d)}") # 字典转集合是key

# 排序可选reverse=True降序，默认是False，升序
print(f"lst排序后是：{sorted(lst)}")
print(f"t排序后是：{sorted(t)}")
print(f"s_str排序后是：{sorted(s_str)}")
print(f"s_set排序后是：{sorted(s_set)}")
print(f"d排序后是：{sorted(d)}") # 字典排序是key

