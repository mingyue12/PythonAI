"""
案例：演示递归入门

递归介绍：
    概述：
        方法自己调用自己的情况就叫递归
    经典案例：
        1.求阶乘
        2.不死神兔，斐波那契数列
        3.文件夹拷贝，删除等。。。
        4.服务器文件整理
    核心要点：
        1.递归必须要有出口，否则会导致死循环
        2.递归调用次数不能过多，否则容易造成死递归
        3.递归必须要有规律
    要点：
        1.分析出口
        2.找规律
求阶乘
    n! = n * (n-1) * ... * 1
    分析流程：
        5! = 5 * 4 * 3 * 2 * 1
"""

def factorial(n):
    # 出口
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    print(factorial(5))

# # 场景1：递归入门案例
# count = 0
# def show():
#     global count
#     count += 1
#     if count >= 100:
#         return
#     print(f'我是show函数！{count}')
#     show()  # 函数自己调用自己
#
# if __name__ == '__main__':
#     show()



