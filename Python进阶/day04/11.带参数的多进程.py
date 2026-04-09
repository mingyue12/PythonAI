"""
案例：演示带参数的多进程

进程传参的两种方式：
    1.通过args参数传参，接受所有的位置参数
    2.通过kwargs参数传参，接受所有的关键字参数

"""
# 导包
import multiprocessing # 导入多进程模块

# 需求：小明一边敲代码，一边听音乐
# 定义函数，表示敲代码
def coding(name, number):
    for i in range(number):
        print(f"{name}在第{i + 1}号任务中编码")

# 定义函数，表示听音乐
def music(name, number):
    for i in range(number):
        print(f"{name}在第{i + 1}号任务中听音乐")


if __name__ == '__main__':
    # 创建两个子进程
    s1 = multiprocessing.Process(target=coding, args=('小明', 5))
    s2 = multiprocessing.Process(target=music, kwargs={'name': '小明', 'number': 5})
    # 启动两个子进程
    s1.start()
    s2.start()

