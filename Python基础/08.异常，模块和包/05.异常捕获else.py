"""
如果抓住异常，则处理
如果没有异常，则也可以有相应处理
"""

try:
    print()
except Exception as e:
    print(f"<UNK>{e}")
else:
    print("正常")