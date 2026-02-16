import modelB as B


# 如果本文件直接执行，则内置变量__name__会被赋值为__main__
# 如果本文件被import或from导入，则内置变量__name__会被赋值为文件名称
if __name__ == '__main__':
    B.say_hi()
    print(B.name)