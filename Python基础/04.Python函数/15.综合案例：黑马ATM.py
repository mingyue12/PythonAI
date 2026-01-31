# 初始化全局变量
num_money = 0
name_str = input("请输入您的姓名：")
print(f"欢迎{name_str}使用黑马ATM")


def print_main_menu():
    """打印主菜单"""
    print("\n========== 黑马ATM ==========")
    print("1. 查询余额")
    print("2. 存款")
    print("3. 取款")
    print("4. 退出")
    print("============================")


def check_money():
    """查询余额"""
    print(f"您好{name_str}，当前余额为：{num_money:.2f} 元")


def save_money():
    """存款功能"""
    global num_money
    try:
        money = float(input("请输入存款金额："))
        if money <= 0:
            print("❌ 存款金额必须大于 0！")
            return
        num_money += money
        print(f"✅ 存款成功！当前余额为：{num_money:.2f} 元")
    except ValueError:
        print("❌ 输入无效，请输入一个有效的数字！")


def get_money():
    """取款功能"""
    global num_money
    try:
        money = float(input(f"您好{name_str}，请输入取款金额："))
        if money <= 0:
            print("❌ 取款金额必须大于 0！")
            return
        if money > num_money:
            print(f"❌ 余额不足！当前余额为 {num_money:.2f} 元，无法取出 {money:.2f} 元。")
        else:
            num_money -= money
            print(f"✅ 取款成功！当前余额为：{num_money:.2f} 元")
    except ValueError:
        print("❌ 输入无效，请输入一个有效的数字！")


# 主程序循环
while True:
    print_main_menu()
    try:
        flag = int(input("请选择服务项目（1-4）："))
    except ValueError:
        print("❌ 请输入数字选项（1-4）！")
        continue  # 跳过本次循环，重新显示菜单

    if flag == 1:
        check_money()
    elif flag == 2:
        save_money()
    elif flag == 3:
        get_money()
    elif flag == 4:
        print("感谢使用黑马ATM，再见！👋")
        break
    else:
        print("❌ 无效选项，请输入 1、2、3 或 4！")


