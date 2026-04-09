"""
案例：演示多进程入门案例

多进程的目的：
    他属于多任务的一种实现方式，目的是充分利用CPU资源，提高程序执行效率

    实现方式：
        1.导入multiprocessing模块
        2.创建进程对象
        3.启动进程
        4.等待进程结束
        5.释放资源
"""

# 导包
import multiprocessing
import time
# 定义函数A
def coding():
    for i in range(1, 11):
        print(f"在第{i}号任务中编码")

# 定义函数B
def music():
    for i in range(1, 11):

        print(f"在第{i}号任务中听音乐")

if __name__ == '__main__':

    # 3.创建两个进程对象，分别关联上述的两个目标函数
    p2 = multiprocessing.Process(target=music)
    p1 = multiprocessing.Process(target=coding)
    # 4.启动进程
    p1.start()
    p2.start()




