import socket
import threading
import time
# 服务器地址和端口
HOST = '192.168.1.6'
PORT = 12345
def start_server():
    # 创建服务器套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 绑定地址和端口
    server_socket.bind((HOST, PORT))
    
    # 监听连接
    server_socket.listen(5)
    print(f"聊天服务器在{HOST}:{PORT}上展开")
    time.sleep(1)
    print("等待连接")
    
    while True:
        # 接受客户端连接
        client_socket, address = server_socket.accept()
        print(f"连接到 {address[0]}:{address[1]}客户端")
        print("聊天愉快")
        print("等待对方发起话题")
        # 创建线程来处理客户端
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

def handle_client(client_socket):
    while True:
        # 接收客户端发送的消息
        data = client_socket.recv(1024).decode()
        if not data:
            break 
        print(f"世界的另一头说：{data}")
        # 处理接收到的消息，回复
        response = input("回复：")
        
        # 发送处理后的消息回客户端
        client_socket.send(response.encode())
        print("等待回复，请不要按回车键")
    # 关闭客户端连接
    client_socket.close()


# 启动服务器
start_server()