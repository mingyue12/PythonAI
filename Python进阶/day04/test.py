import socket

# 1. 创建客户端Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 连接服务端

client_socket.connect(('47.109.28.19', 8811))
print("客户端连接成功")  # 加日志，确认连接成功

# 4. 接收服务端消息
data = client_socket.recv(1024).decode('utf-8')
print(f'客户端收到来自服务端的信息: {data}')

# 3. 给服务端发消息
client_socket.send(b'Hello Server')
print(f'客户端给服务端发送消息: b"Hello Server"')



# 5. 释放资源
client_socket.close()