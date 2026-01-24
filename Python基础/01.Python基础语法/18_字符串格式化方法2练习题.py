"""
    使用f——format方式进行格式化字符串
"""

money = 100
name = "周杰伦"
salary = 18000.55

# f"{变量:精度}"

print(f"我是{name},钱包余额{money},今天发工资{salary:10.1f}元，钱包剩余：{money+salary}")
