

def check_age(age):
    if age < 18:
        return None
    return "SUCCESS"


if check_age(10):
    print("成年")
else:
    print("未成年")

"""
只要不是0，False，None，空字符串
其余都是True
"""
