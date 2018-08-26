from threading import Thread,Lock
import time

num = 0
def work1():
	global num
	m.acquire(True) #加锁,阻塞加锁
	for i in range(1000000):
		num += 1
	m.release() #释放锁
	print(num)

def work2():
	global num
	m.acquire(True)
	for i in range(1000000):
		num += 1
	m.release() #释放锁
	print(num)

m = Lock()
t1 = Thread(target=work1)
t1.start()

t2 = Thread(target=work2)
t2.start()
