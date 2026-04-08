"""
案例：多个装饰器装饰一个函数

记忆：
    多个装饰器装饰一个函数，是按照由内向外的顺序来装饰的，
    但如果你要是用装饰器的写法来做，看到的效果是从上往下执行的
"""

# 需求发表评论前，需要先登录，再验证验证码，请用所学，模拟该功能
# 1.定义装饰器，表示登录
def check_login(fn_name):
    # 定义内部函数
    def fn_inner():
        # 额外功能
        print("登录成功")
        # 调用原函数，引用
        fn_name()
    return fn_inner

# 2.定义装饰器表示验证码
def check_code(fn_name):
    # 定义内部函数
    def fn_inner():
        # 额外功能
        print("验证码验证成功")
        # 调用原函数，引用
        fn_name()
    return fn_inner



# 3.定义函数，表示发表评论
@check_login
@check_code
def comment():
    print("发表评论")

