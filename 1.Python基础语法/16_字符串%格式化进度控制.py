"""
    m.n精度控制
    - m控制宽度，n控制小数点后位数
"""

age = 11
height = 172.567
name = "周杰伦"

print("年龄%5d岁" % age)  # 5个字符宽度，右对齐

print("年龄%1d岁" % age)  # 字符宽度小于数字位数，精度控制不生效

print("年龄%3.2d岁" % age)  # 整数对小数精度控制不理会

print("身高%3.2d米" % height)  # 用整数接收小数，则小数部分丢失.n控制不生效，m控制生效。

print("-" * 20)

# zong
print("身高%7.2fcm" % height)  # .2f控制小数点后两位
