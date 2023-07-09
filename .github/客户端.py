import socket

# 服务器地址和端口
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

def start_client():
    # 创建客户端套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 连接服务器
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"Connected to {SERVER_HOST}:{SERVER_PORT}")
    
    while True:
        # 输入要发送的消息
        message = input("发送: ")
        
        if message == 'quit':
            break
    
        # 发送消息给服务器
        client_socket.send(message.encode())
        while True:    
            # 接收服务器返回的消息
            response = client_socket.recv(1024).decode()
        
            # 打印服务器返回的消息
            print(f"服务器回复: {response}")
    
    # 关闭客户端连接
    client_socket.close()

# 启动客户端
start_client()