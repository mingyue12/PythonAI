# 字典的常用操作方法
# 新增元素
d = {"周杰伦": 99, "王力宏": 88, "林俊杰": 66}
print(d)
# 新增元素
d["陈奕迅"] = 77
print(d)

# 更新元素
d["周杰伦"] = 100
print(d)

# 删除元素
name = d.pop("王力宏")
print(name)
print(d)

# 得到所有的key值
keys = d.keys()
print(keys)

# 得到所有的value值
values = d.values()
print(values)

# 得到所有的键值对
items = d.items()
print(items)

# 遍历字典
for key in d.keys():
    print(key, d[key])

# 得到字典的长度
print(len(d))

# 清空字典
d.clear()
d = {}
