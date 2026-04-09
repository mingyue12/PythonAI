"""
案例：演示编解码

细节：
    1.编码 = 把字符串转换为字节序列
        '字符串'.encode(码表)
    2.解码 = 把字节序列转换为字符串
        字节序列.decode(码表)
    3.只要乱码了，原因只有1个，编解码不同
    4.英文字母。数字。特殊符号无论什么码表都只占1个字节，中文在gbk占两个字节，utf-8中占用3个字节
    5.二进制数据特殊写法，即：b'字节序列'，对中文无效
"""
# 需求1：编码
# s1 = '黑马'
s1 = '黑马123abCD!@#'

print(s1.encode())          # b'黑马'
print(s1.encode('utf-8'))   # b'黑马'
print(s1.encode('gbk'))     # b'黑马'
print("-" * 50)

# 需求2：解码

bys = b'\xe9\xbb\x91\xe9\xa9\xac123abCD!@#'
print(type(bys))

s2 = bys.decode()
s3 = bys.decode('utf-8')
print(s2)
print(s3)
print('-' * 50)

s4 = bys.decode('gbk')
print(s4)           # 榛戦┈123abCD!@#


