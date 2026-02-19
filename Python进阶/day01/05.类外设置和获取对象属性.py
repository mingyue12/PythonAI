"""
案例：类外设置和获取对象属性

类外设置对象属性的格式：
对象名.属性名 = 值
"""
# 创建汽车对象
class Car:
    # 属性

    # 行为
    def run(self):
        print("汽车在跑...")


# 创建汽车对象
c1 = Car()
c1.run()
c1.color = "黄色"
c1.num = 4
print(f"颜色{c1.color}，轮胎数{c1.num}")
print("-" * 34)

# 继续创建汽车对象
c2 = Car()
c2.run()

print("-" * 34)