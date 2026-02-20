"""
案例：烤地瓜
需求：
    1. 定义地瓜类 -> SweetPotato
    2. 属性：被烤时间cook_time,状态cook_status,调料condiments
    3. 行为：cook()烤地瓜,添加调料add_condiments()
    4. 魔法方法：__init__() -> 初始化属性,__str__() -> 打印对象信息
    5. 规则：
        烘焙时间        地瓜状态
        [0, 3)        生的
        [3, 7)        半生的
        [7, 12)        熟的
        超过12分钟        烤糊了
"""
class SweetPotato:
    # init函数初始化
    def __init__(self):
        self.cook_time = 0
        self.cook_status = "生的"
        self.condiments = []


    def cook(self, time):

        # 根据烘烤时间修改地瓜状态
        if time <= 0:
            print('无效值！')
        else:
            # 修改地瓜的烘焙时间
            self.cook_time += time
            if 0 <= self.cook_time < 3:
                self.cook_status = "生的"
            elif 3 <= self.cook_time < 7:
                self.cook_status = "半生不熟"
            elif 7 <= self.cook_time < 12:
                self.cook_status = "熟了"
            else:
                self.cook_status = "糊了"

    # 添加调料
    def add_condiments(self, condiment):
        self.condiments.append(condiment)


    # 重写__str__()函数，打印对象信息
    def __str__(self):
        return f'烘烤时间：{self.cook_time}，烘烤状态{self.cook_status}，调料{self.condiments}'


# 测试
if __name__ == '__main__':
    sweetpotato = SweetPotato()
    # 烘烤
    sweetpotato.cook(5)    # 添加调料
    # 添加调料
    sweetpotato.add_condiments('盐')
    sweetpotato.add_condiments('糖')
    sweetpotato.add_condiments('辣椒面')
    # 打印对象信息
    print(sweetpotato)
