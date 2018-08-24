from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.sendto("我是老邵",encode("gb2312"),("10.114.25.240",8444))
s.socket()