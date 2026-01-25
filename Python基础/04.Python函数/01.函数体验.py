def my_len(data):
    """
    计算输入数据的长度
    参数:
        data: 需要计算长度的可迭代对象
    返回:
        data的长度
    """
    my_length: int = 0  # 初始化长度计数器为0
    for value in data:  # 遍历data中的每个元素
        my_length += 1  # 每遍历一个元素，长度计数器加1
    return my_length  # 返回计算得到的长度


name = "itheima"
length = 0
for i in name:
    length += 1
print(f"{name}的长度是{length}")

info = "我爱学习"
print(f"{info}的长度是{my_len(info)}")
