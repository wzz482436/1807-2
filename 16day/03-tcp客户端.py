from socket import *
ip=input("请输入连接的ip地址")
port=int(input("请输入端口: "))

s = socket(AF_INET,SOCK_STREAM)
s.connect((ip,port))
while True:
	msg = input("请输入发送内容")
	s.send(msg.encode("gb2312"))
	msg = s.recv(1024).decode("gb2312")
	print("收到信息: %s"%msg)
