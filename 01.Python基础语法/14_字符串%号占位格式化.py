"""
    %占位格式化（拼接）
"""
name = "周杰伦"
age = 18
height = 172.25

# 传统拼接
info1 = name + "今年" + str(age) + "岁，身高" + str(height) + "米"
print(info1)

# %占位格式化，如果提供数字类型，则会自动转为字符串
message1 = "我是%s" % name
info2 = "我是%s今年%5d岁，身高%.6f米" % (name, age, height)     # 变量超过一个要用（）括起来
print(info2)
print(message1)

# %s转化成字符串，%d转化成整数，%f转化成浮点数，放入占位符位置,也可以进行精度控制。

