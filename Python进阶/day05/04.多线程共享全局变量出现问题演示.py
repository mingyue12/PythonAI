"""
案例：演示多线程共享全局变量，可能出现的问题

多线程共享全局变量，出现的问题：
    累加次数不够
产生原因：
    线程1还没有来得及执行完前，被线程2抢走了资源，就可能出问题


解决方案：
    加互斥锁

细节：
    1.加锁和解锁，必须成对出现，要在合适的时机释放锁，否则会导致死锁，或锁不住

"""


# 需求：定义两个函数，分别对全局变量；累加100万次，创建两个线程，执行观看效果
# 导包
import threading

# 1.定义全局变量
global_var = 0

# 创建线程锁
mutex_lock = threading.Lock()

# 2.定义目标函1，累加100万次
def target_func1():
    # 加锁
    mutex_lock.acquire()

    global global_var
    for i in range(10000000):
        global_var += 1
    print(f"线程1累加次数：{global_var}")
    # 解锁
    mutex_lock.release()



# 3.定义目标函2，累加100万次
def target_func2():
    # 加锁
    mutex_lock.acquire()

    global global_var
    for i in range(10000000):
        global_var += 1
    print(f"线程2累加次数：{global_var}")

    # 解锁
    mutex_lock.release()

# 测试
if __name__ == '__main__':
    t1 = threading.Thread(target=target_func1)
    t2 = threading.Thread(target=target_func2)
    t1.start()
    t2.start()

