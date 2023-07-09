import socket
import threading
# 服务器地址和端口
SERVER_HOST = '192.168.1.6'
SERVER_PORT = 12345
timeout = 10
try:
    sock = socket.create_connection((SERVER_HOST, SERVER_PORT), timeout)
    print("连接服务器成功")
    # 连接成功后可以进行其他操作
except socket.error as e:
    print("连接服务器失败请重启或者检查网络:", e)
def start_client():
    # 创建客户端套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 连接服务器
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"连接到 :{SERVER_HOST}:{SERVER_PORT}")
    
    while True:
        # 输入要发送的消息
        message = input("发送: ")
        # 发送消息给服务器
        client_socket.send(message.encode())
        print("等待回复，请不要按回车键")
        # 接收服务器返回的消息
        response = client_socket.recv(1024).decode()
    
        # 打印服务器返回的消息
        print(f"世界的另一头说: {response}")
    
    # 关闭客户端连接
    client_socket.close()

# 启动客户端
start_client()