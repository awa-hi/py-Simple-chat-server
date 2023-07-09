import socket
import threading

# 服务器地址和端口
HOST = '127.0.0.1'
PORT = 12345
def start_server():
    # 创建服务器套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 绑定地址和端口
    server_socket.bind((HOST, PORT))
    
    # 监听连接
    server_socket.listen(5)
    print(f"Server started on {HOST}:{PORT}")
    
    while True:
        # 接受客户端连接
        client_socket, address = server_socket.accept()
        print(f"Connected with {address[0]}:{address[1]}")
        
        # 创建线程来处理客户端
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

def handle_client(client_socket):
    while True:
        # 接收客户端发送的消息
        data = client_socket.recv(1024).decode()
        if not data:
            break 
        print(f"客户端说{data}")
       
        # 处理接收到的消息，回复
        response = input("回复：")
        
        # 发送处理后的消息回客户端
        client_socket.send(response.encode())
    
    # 关闭客户端连接
    client_socket.close()


# 启动服务器
start_server()