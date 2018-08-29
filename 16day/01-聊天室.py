from threading import Thread
from socket import *
s=socket(AF_INET, SOCK_DGRAM)
#AF_INET --------IPV4
#SOCK_DGRAM -------UDP
ip = input("请输入对方ip:")
port = int(input("请输入对方端口:"))
s.bind(("",8080))

def send():
	while True:
		msg=input("请输入发送内容")
		s.sendto(msg.encode("gb2312"),(ip,port))



def jieshou():
	while True:


		msg = s.recvfrom(1024)
		#(dsad,("129...",8080))

		print("收到消息: %s"%msg[0].decode("gb2312"))

		#print(msg[0].decode('gb2312')) #打印发送的内容
		#print(msg[1][0]) #打印本机ip地址
		

t = Thread(target=jieshou)
t.start()

t1 =Thread(target=send)
t1.start()

t.join()
t1.join()
