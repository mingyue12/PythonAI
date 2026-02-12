# 可以捕获多个异常，但是无法区分
try:
    1 / 0
    f = open("test.txt", "r")
except (ZeroDivisionError, FileExistsError) as e:
    print("有异常了，异常是：", e)

# 捕获多个异常同时区分
try:
    # 这个try块中可能触发3种不同异常
    d = {}
    print(d["name"])  # 操作1：触发 KeyError（字典无此键）
    10 / 0  # 操作2：触发 ZeroDivisionError（除零）
    open("test.txt", "r")  # 操作3：触发 FileNotFoundError（文件不存在）
    # 按顺序匹配异常类型，精准区分处理
except KeyError as e:
    print(f"捕获到字典键异常：{e}")
except ZeroDivisionError as e:
    print(f"捕获到除零异常：{e}")
except FileNotFoundError as e:
    print(f"捕获到文件未找到异常：{e}")
