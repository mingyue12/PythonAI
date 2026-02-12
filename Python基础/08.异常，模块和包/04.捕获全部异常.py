"""
需求：不管具体是什么异常，出现就捕获
"""
try:
    1/0
except Exception as e:
    print("出现问题了，问题是：", e)