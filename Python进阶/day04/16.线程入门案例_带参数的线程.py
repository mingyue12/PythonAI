"""
案例：演示线程入门案例,一边听音乐一边写代码

线程使用步骤：
    1.导入线程模块
    2.创建线程对象
    3.启动线程

线程和进程的关系：
    1.进程是CPU分配资源的基本单位
    2.线程是进程中的一个执行流，是CPU调度和执行的基本单位
        线程是依附于进程的
    3.进程间数据相互隔离，线程间数据共享
"""
# 导包
import threading


# 1.定义函数，表示：线程的目标函数
def work(name, num):
    for i in range(1, num + 1):
        print(f"{name}正在努力工作中......{i}")

def music(name, count):
    for i in range(1, count + 1):
        print(f"{name}正在努力听音乐......{i}")

if __name__ == '__main__':
    # 2.创建线程对象
    t1 = threading.Thread(target=work, args=("刘亦菲", 10))
    t2 = threading.Thread(target=music, args=("张三", 10))
    # 3.启动线程
    t1.start()
    t2.start()
