"""
案例：文件上传_服务器端

回顾：网编服务器端实现流程
    1.创建服务器端socket对象
    2.绑定ip和端口号
    3.设置最大监听数
    4.等待客户端申请建立链接
    5.读取客户端上传的（文件）数据
    6.把读取到的数据写到目的地文件中
    7.释放资源
"""

# 导包
import socket

# 创建客户端端socket对象,IPV4，TCP协议
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 链接服务器端ip和端口号
client_sock.connect(('47.109.28.19', 8811))
# 关联数据源文件
with open('./data/1.txt', 'rb') as src_f:
    # 循环读取内容
    while True:
        # 具体操作
        data = src_f.read(8192)
        # 把读取到的数据写给服务器端
        client_sock.send(data)
        # 判断是否读取到数据，无数据结束即可
        if len(data) == 0:
            break

# 接受服务器文件上穿成功绘制
# data = client_sock.recv(1024).decode('utf8')
# print(data)
# 释放资源
client_sock.close()





