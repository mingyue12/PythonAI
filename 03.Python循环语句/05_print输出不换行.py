"""
print(num, end=" ")
end是print的一个形式参数，它决定了输出内容的最后是什么
默认我们是没有使用end参数，则它的值是：\n
如果不需要自动带有\n效果，可以使用end=？修改，比如end=""最后什么都不输出
"""

# print语句的默认效果
print("Hello World", end="\n")
# 不换行可以
print("Hello", end=" ")
print("World", end="")
