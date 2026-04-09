"""
案例：演示单任务，前面不执行完毕，后面绝对无法执行

"""


# 1.定义函数A，输出十次hello world
def fn_A():
    for i in range(10):
        print("hello world")


# 2.定义函数B，输出十次hello python
def fn_B():
    for i in range(10):
        print("hello python")

# 测试
if __name__ == '__main__':
    fn_A()
    fn_B()