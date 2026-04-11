"""
    问，2，3，4能组合成的四位数有几种情况，按照5个一行输出。
    戏为:
要求同时包含1,2,3,4这四个数字.
    1234, 1324均可1122,1123 不行2.要求数1和3不能挨，
    1324,3124不行
    1234, 3412可以
    3，数4不能开头，
    4，5行以内搞定(包括5行)
"""
from itertools import count

count = 0
for i in range(1234, 4322):
    s = str(i)  # 转换为字符串
    if '1' in s and '2' in s and '3' in s and '4' in s and '13' not in s and '31' not in s and s[0] != '4':
        count += 1
        print(s, end='\n' if count % 5 == 0 else '\t')
