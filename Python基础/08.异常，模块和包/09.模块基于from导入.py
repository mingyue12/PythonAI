"""
from 模块01 import f01 as 别名
"""
# 从random模块导入randint函数
# 可以直接使用randint函数
# 可以使用as给函数设置别名
from random import randint as r

# 需求用random模块的randint生成随机数
r(1, 10)
