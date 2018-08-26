from threading import Thread
import time

num = 0
flag = 1 #再加个变量也可以调试bug
def work1():
	global num,flag
	if flag == 1:
		for i in range(1000000):
			num += 1	
		print("thread-1")
		print(num)
		flag += 1
		time.sleep(1)

def work2():
	global num
	while True:
		if flag == 2:
			for i in range(1000000):
				num += 1
			print("thread-2")	
			print(num)
			break
			time.sleep(1)

t1 = Thread(target=work1)
t1.start()
#t1.join() 使用join也可以调试bug

t2 = Thread(target=work2)
t2.start()
