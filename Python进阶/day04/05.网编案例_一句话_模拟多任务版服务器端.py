"""
案例：网编入门案例，服务器端给客户端发送信息，客户端给出回执信息

服务器端开发流程：
    1.创建服务器端Socket对象
    2.绑定IP地址和端口号
    3.设置最大监听数
    4.等待客户端申请建立连接
    5.给客户端发送消息
    6.接收客户端的信息并打印
    7.释放资源
细节：
    客户端和服务器端是通过字节流（bytes）形式实现的
"""
# 导包
import socket

# 1.创建服务器端Socket对象,IPV4，TCP
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.绑定IP地址和端口号
server_sock.bind(('47.109.28.19', 8811))

# 3.设置最大监听数
server_sock.listen(5)

while True:
    try:
        # 4.等待客户端申请建立连接
        accept_socket, client_info = server_sock.accept()

        # 5.给客户端发送消息
        accept_socket.send(b'Welcome To Socket')

        # 6.接收客户端的信息并打印
        data = accept_socket.recv(1024).decode('utf-8')
        print(f'服务器端收到来自{client_info}的信息{data}')

        # 7.释放资源
        accept_socket.close()
    except:
        pass

# 扩展： 设置端口号复用，目的是快速重启服务（服务器关闭后立即释放端口）
# 参1：SOL_SOCKET，表示套接字选项
# 参2：SO_REUSEADDR，表示复用地址
# 参3：1，表示开启
# server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
