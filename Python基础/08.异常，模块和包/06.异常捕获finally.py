"""
不管有没有异常必做的事情 finally
"""

try:
    1/0
except Exception as e:
    print(f"<UNK>{e}")
else:
    print("一切正常")
finally:
    print("有没有问题我都会执行")