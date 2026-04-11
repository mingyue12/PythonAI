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
# 导包
import threading
import time

# 1.定义目标函数
def work():
    for i in range(10):
        time.sleep(0.2)
        print(f"正在努力工作中......{i}")

if __name__ == '__main__':
    # 2.1 创建线程对象
    # 守护线程写法1：在创建线程对象时，设置daemon参数为True
    # 守护线程：主线程结束时，守护线程会自动结束
    # t = threading.Thread(target=work, name="刘亦菲", daemon=True)
    t = threading.Thread(target=work, name="刘亦菲")
    # 写法2:setdaemon属性为True
    t.daemon = True
    # 2.2 启动线程
    t.start()
    # 2.3 设置主线程休眠时间1s
    time.sleep(1)
    # 2.4 设置主线程结束标记
    print("主线程结束")

