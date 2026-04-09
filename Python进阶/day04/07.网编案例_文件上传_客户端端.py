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

# 创建服务器端socket对象
server_sock = socket.socket()
# 绑定ip和端口号
server_sock.bind(('47.109.28.19', 8811))
# 设置最大监听数
server_sock.listen(5)
# 等待客户端申请建立连接
while True:
    try:
        accept_socket, client_info = server_sock.accept()
        # 接收客户端上传的（文件）数据
        # 循环读取数据
        # 把接受到的数据写到目的地文件中
        # 关联目的地文件
        with open(f'./data/{client_info[0]}.txt', 'wb') as dest_f:
            while True:
                # 接受客户端上传的文件数据
                bys = accept_socket.recv(81924) # 8192字节 = 8KB
                # 判断是否接受到数据，无数据结束即可
                if len(bys) == 0:
                    break
                # 把接受到的数据写到目的地文件中
                dest_f.write(bys)
        # 释放资源
        accept_socket.close()
    except:
        pass






