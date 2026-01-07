def ascii_converter():
    while True:
        # 接收用户输入
        user_input = input("请输入要转换的单个字符（输入'q'或'Q'退出程序）：")

        # 退出条件判断
        if user_input.lower() == 'q':
            print("程序已退出！")
            break

        # 验证输入是否为单个字符
        if len(user_input) != 1:
            print("错误：请输入单个字符，不要输入多个字符或空值！")
            continue

        # 获取ASCII十进制值
        ascii_dec = ord(user_input)
        # 转换为十六进制值（大写形式，符合ASCII表规范）
        ascii_hex = hex(ascii_dec).upper().replace('0X', '')

        # 补充十六进制为两位显示（与ASCII表格式一致）
        if len(ascii_hex) == 1:
            ascii_hex = '0' + ascii_hex

        # 输出结果
        print(f"字符 '{user_input}' 的ASCII值：")
        print(f"  十进制：{ascii_dec}")
        print(f"  十六进制：{ascii_hex}")
        print("-" * 30)


# 运行工具
if __name__ == "__main__":
    print("===== ASCII码实用换算小工具 =====")
    ascii_converter()
