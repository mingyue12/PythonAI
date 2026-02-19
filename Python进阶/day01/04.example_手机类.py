"""
案例：定义手机类，能开机，关机，拍照
"""

class Phone:
    # 属性

    # 行为
    def power_on(self):
        print(f"{self}手机会开机... ...")

    def power_off(self):
        print(f"{self}手机会关机... ...")

    def take_photo(self):
        print(f"{self}手机会拍照... ...")


# 2.创建手机对象
p1 = Phone()
print(f"p1：{p1}")
print(f"p1对象的地址值是：{id(p1)}")
print("-" * 34)
# 调用手机对象的方法
p1.power_on()
p1.take_photo()
p1.power_off()
print("-" * 34)

# 3.再次创建手机对象
p2 = Phone()
print(f"p2：{p2}")
print(f"p2对象的地址值是：{id(p2)}")
print("-" * 34)
# 调用手机对象的方法
p2.power_on()
p2.take_photo()
p2.power_off()
print("-" * 34)
