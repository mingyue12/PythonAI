"""
案例：多态案例_战斗平台

需求：
    1.构建对战平台（公共的函数）object_play(),接受英雄机和敌机
    2.在不修改对站平台的代码情况下，完成多次战斗
    3.规则：
        英雄机，一代战斗机战斗力60，二代80
        敌机，1代70

代码提示：
    英雄机1 HeroFighter
    英雄机2 AdvHeroFighter
    敌机    EnemyFighter
"""
from math import expm1


# 1.定义英雄机一代，战斗力 60
class HeroFighter:
    def power(self):
        return 60

# 2.定义英雄机二代，战斗力 80
class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80

# 3.敌机一代，战斗力 70
class EnemyFighter:
    def power(self):
        return 70

def object_play(hero:HeroFighter, enemy:EnemyFighter):
    if hero.power() >= enemy.power():
        print("英雄机赢了")
    else:
        print("英雄机输了")
# 4.构建对战平台，公共函数，接受不同参数，有不同效果
if __name__ == '__main__':
    # 思路1：不使用对战平台完成对战
    # 场景1： 英雄机一代vs敌机一代
    # 场景2： 英雄机二代vs敌机一代
    h1 = HeroFighter()
    h2 = AdvHeroFighter()
    e1 = EnemyFighter()
    # 场景1： 英雄机一代vs敌机一代
    if h1.power() >= e1.power():
        print("英雄机一代赢了")
    else:
        print("英雄机一代输了")
    print("-" * 34)
    # 场景2： 英雄机二代vs敌机一代
    if h2.power() >= e1.power():
        print("英雄机二代赢了")
    else:
        print("英雄机二代输了")
    print("*" * 34)

    # 思路2：使用对战平台完成对战
    object_play(h1, e1)
    object_play(h2, e1)
