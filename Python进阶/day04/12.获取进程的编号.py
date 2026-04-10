"""
案例：获取进程的编号

概述：
    在设备中，每个进程都有自己的唯一进程id，当程序释放的时候，该进程id也会释放，即：进程id是可以重复使用的
目的：
    1.查看子进程和父进程的关系，方便管理
    2.例如：杀死指定进程，创建子进程...
格式：
    查看当前进程pid：
        OS模块(operating,系统级模块)的.getpid()方法
        multiprocessing.Process()   #current_process()的pid属性
    查看当前进程的ppid：    parent process id(父进程id)
        os.getppid()

细节：
    main中创建的进程，如果没有特殊指定，它的父进程都是main进程，
    而main进程的父进程是Pycharm的程序pid
"""

# 导包
import multiprocessing  # 导入多进程模块
import os               # 导入系统模块

# 需求：小明一边敲代码，一边听音乐
# 定义函数，表示敲代码
def coding(name, number):
    for i in range(number):
        print(f"{name}在第{i + 1}号任务中编码")
    print(f'p1进程的pid是：{os.getpid()},{multiprocessing.current_process().pid},父进程id为：{os.getppid()}')

# 定义函数，表示听音乐
def music(name, number):
    for i in range(number):
        print(f"{name}在第{i + 1}号任务中听音乐")
    print(f'p2进程的pid是：{os.getpid()},{multiprocessing.current_process().pid},父进程id为：{os.getppid()}')


if __name__ == '__main__':
    # 创建两个子进程
    s1 = multiprocessing.Process(target=coding, args=('小明', 5))
    s2 = multiprocessing.Process(target=music, kwargs={'name': '小明', 'number': 5})
    # 启动两个子进程
    s1.start()
    s2.start()
    #  查看主进程信息
    print(f'主进程的pid是：{os.getpid()},{multiprocessing.current_process().pid},父进程id为：{os.getppid()}')
