"""
案例：演示多线程特点
随机性：线程的执行顺序是随机的，不能保证线程的执行顺序是固定的。

多线程特点：
    1.线程执行具有随机性，原因是因为CPU在做着高效的切换
    2.默认情况下，主线程会等待子线程结束再结束
    3.（同一个进程的线程之间，是共享数据的）
    4.多线程操作共享数据，可能会出现安全问题，可以用互斥锁解决问题

CPU调度资源的策略：
    1.均分时间片
    2.抢占式调度
"""

# 需求：定义全局变量my_list = [],定义两个目标函数分别实现，
# 添加查看数据，最后创建两个线程，分别执行对应任务观察结果

# 导包
import time
import threading
from time import sleep

# 定义列表
my_list = []
# 定义write_data函数
def write_data():
    for i in range(10):
        my_list.append(i)
        print(f"写入数据：{i}")

# 定义read_data函数
def read_data():
    sleep(1)
    for i in range(10):
        print(f"读取数据：{my_list[i]}")
    print(1)

if __name__ == '__main__':
    # 2.创建线程对象
    t1 = threading.Thread(target=write_data)
    t2 = threading.Thread(target=read_data)
    # 3.启动线程
    t1.start()
    t2.start()
