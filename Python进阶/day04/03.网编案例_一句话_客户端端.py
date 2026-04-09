"""
案例：网编入门案例，服务器端给客户端发送信息，客户端给出回执信息

客户端开发流程：
    1.创建客户端Socket对象
    2.链接服务器端，指定ip，端口号
    3.接收服务器端的信息并打印
    4.给服务器端发送消息
    5.释放资源
细节：
    客户端和服务器端是通过字节流（bytes）形式实现的
"""
# 导包
import socket

# 1.创建客户端Socket对象IPV4，TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.链接服务器端，指定ip，端口号
client_socket.connect(('47.109.28.19', 8811))
# 3.接收服务器端的信息并打印
data = client_socket.recv(1024).decode('utf-8')
print(f'客户端收到来自服务器端的信息{data}')

# 4.给服务器端发送消息
client_socket.send('你好服务器'.encode('utf-8'))
print(f'客户端给服务器端发送消息: 你好服务器')

# 5.释放资源
client_socket.close()
