"""
语法：
range(起始值，结束值，步长)
获得数字序列，可被迭代。
"""

for i in range(5):
    print(i,end=" ")

print()
print("-" * 10)

for i in range(5, 10):
    print(i,end=" ")

print()
print("-" * 10)

for i in range(5, 20, 2):
    print(i,end=" ")
