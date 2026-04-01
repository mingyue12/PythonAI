"""
nonlocal关键字介绍:
    他是Python内置的关键字，可以实现在内部函数中修改外部函数的变量值

"""

# 需求：编写一个闭包，让内部函数访问外部函数的参数a = 100，并观察结果

# 1.定义外部函数
def fn_outer():
    # 2.定义外部函数（局部）变量
    a = 100

    # 3.定义内部函数，访问外部函数的变量
    def fn_inner():
        # 4.在内部函数中修改外部函数变量
        nonlocal a  # 声明a为非局部变量，即外部函数的变量
        a += 1
        # 5.打印外部函数的变量
        print(f"a = {a}")
    # 6.返回内部函数对象
    return fn_inner


# 7.测试
if __name__ == '__main__':
    fn_inner = fn_outer()
    fn_inner()    # a = 101
    fn_inner()    # a = 102





