"""
案例：演示进程的特点：

进程的特点：
    1.进程之间数据隔离，互不干扰
        子进程相当于是父进程的副本，会将父进程的main外资源拷贝一份，
        即：各是各的，互不干扰，互不共享
    2.默认情况下，主进程会等待子进程执行完毕，才会结束

"""
# 导包
import multiprocessing

# 需求：定义一个公共的容器my_list_container = []
# 一个进程向容器中添加数据，另一个进程从容器中读取数据，观察结果
# 1.创建公共容器
my_list_container_container = []

# 2.定义函数，表示向容器中添加数据
def add_data_to_container():
    for i in range(1, 6):
        my_list_container_container.append(i)
        print(f"向容器中添加数据：{i}")

    print(my_list_container_container)


# 3.定义函数，表示从容器中读取数据
def read_data_from_container():
    print(my_list_container_container)

# 测试
if __name__ == '__main__':
    # 4.创建子进程
    p2 = multiprocessing.Process(target=read_data_from_container)
    p1 = multiprocessing.Process(target=add_data_to_container)
    # 5.启动子进程
    p1.start()
    p2.start()

