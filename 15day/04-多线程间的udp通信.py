from threading import Thread
from socket import *
s=socket(AF_INET, SOCK_DGRAM)
def jieshou():

	s.sendto("苏柚柚".encode("gb2312"),("192.168.43.250",8080))
	while True:
		recvData = s.recvfrom(1024)
		#(dsad,("129...",8080))
		print(recvData[0].decode('gb2312')) #打印发送的内容
		print(recvData[1][0]) #打印本机ip地址
		print(recvData[1][1]) #打印本地端口号

	s.close()

def send():
	s.sendto("老王".encode("gb2312"),("192.168.43.250",8080))

	s.close()

t = Thread(target=jieshou)
t.start()

t1 =Thread(target=send)
t1.start()


