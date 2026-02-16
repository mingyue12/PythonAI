# 在_init_.py中
# __all__内置变量默认是None
# 如果__all__变量被赋值为一个列表，那么在from 包名 import *时，只有列表中的模块名会被导入
__all__ = ["model1"]