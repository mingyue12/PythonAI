
num_money = None
name_str = str(input("请输入您的姓名："))
print(f"欢迎{name_str}使用黑马ATM")


def save_money():   # 存款函数
    global num_money
    if num_money is None:
        num_money = 0
    money = float(input("请输入存款金额："))
    num_money += money
    print(f"存款成功，当前余额为：{num_money}")


def print_main_menu():  # 打印主菜单函数
    print("==========黑马ATM==========")
    print("1.查询余额")
    print("2.存款")
    print("3.取款")
    print("4.退出")
    print("==========================")


def check_money():  # 查询余额函数
    global num_money
    if num_money is None:
        num_money = 0
    print(f"您好{name_str},当前余额为：{num_money}")


def get_money():  # 取款函数
    global num_money
    if num_money is None:
        num_money = 0
    money = float(input(f"您好{name_str},请输入取款金额："))
    if money > num_money:
        print(f"您好{name_str},余额不足，取款失败")
    else:
        num_money -= money
        print(f"您好{name_str},取款成功，当前余额为：{num_money}")


while True:
    print_main_menu()
    flag = int(input("欢迎使用黑马ATM，请选择服务项目"))
    if flag == 1:
        print("查询余额")
        check_money()
    elif flag == 2:
        print("存款")
        save_money()
    elif flag == 3:
        print("取款")
        get_money()
    elif flag == 4:
        print("退出")
        break
    else:
        print("输入有误，请重新选择")



