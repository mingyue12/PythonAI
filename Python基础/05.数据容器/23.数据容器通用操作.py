# 通用操作
# 1. len() 获取容器中元素个数
# 2. del() 删除指定元素
# 3. in 判断元素是否在容器中
# 4. + 两个容器相加
# 5. * 重复元素
# 6. max() 获取最大值
# 7. min() 获取最小值
# 8. sorted() 排序
# 9. reversed() 反转
# 10. sum() 求和
# 11. enumerate() 枚举
# 12. zip() 拉链


# 找出最大值
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
s_str = "hello"
s_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
d = {
    "1": 1,
    "2": 2,
    "3": 3,
}

print(f"列表最大值：{max(lst)}")
print(f"元组最大值：{max(t)}")
print(f"字符串最大值：{max(s_str)}")
print(f"集合最大值：{max(s_set)}")
print(f"字典最大值：{max(d.values())}")

# 找出最小值
print(f"列表最小值：{min(lst)}")
print(f"元组最小值：{min(t)}")
print(f"字符串最小值：{min(s_str)}")
print(f"集合最小值：{min(s_set)}")
print(f"字典最小值：{min(d.values())}")

# 转列表
print(f"元组转列表：{list(t)}")
print(f"字符串转列表：{list(s_str)}")
print(f"集合转列表：{list(s_set)}")
print(f"字典转列表：{list(d)}")

# 转元组
print(f"列表转元组：{tuple(lst)}")
print(f"字符串转元组：{tuple(s_str)}")
print(f"集合转元组：{tuple(s_set)}")
print(f"字典转元组：{tuple(d)}")

# 转字符串
print(f"列表转字符串：{str(lst)}")
print(f"元组转字符串：{str(t)}")
print(f"集合转字符串：{str(s_set)}")
print(f"字典转字符串：{str(d)}")

# 转集合
print(f"列表转集合：{set(lst)}")
print(f"元组转集合：{set(t)}")
print(f"字符串转集合：{set(s_str)}")
print(f"字典转集合：{set(d)}")
