from threading import Thread
from socket import *

s = socket(AF_INET,SOCK_DGRAM)
ip = input("输入IP地址:")
port = int(input("输入端口:"))
s.bind("",6778)

def send():
    while True:
        msg = input("输入发送内容:")
        s.endto(msg.encode("gb2312"),(ip,port))

def recv():
    while True:
        msg = s.recv(1024)
        print("收到消息:%s"%msg[0].decode("gb2312"))

t1 = Thread(target=send)
t2 = Thread(target=recv)
t1.start()
t2.start()
t1.join()
t2.join()