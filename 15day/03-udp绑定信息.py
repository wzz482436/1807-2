from socket import *
s=socket(AF_INET, SOCK_DGRAM)
s.sendto("苏柚柚".encode("gb2312"),("192.168.43.250",8080))
while True:
	recvData = s.recvfrom(1024)
	print(recvData[0].decode('gb2312')) #打印发送的内容
	print(recvData[1][0]) #打印本机ip地址
	print(recvData[1][1]) #打印本地端口号

	#print((recvData[0].decode('gb2312'),recvData[1][0],recvData[1][1])) #打印元组格式
s.close()


