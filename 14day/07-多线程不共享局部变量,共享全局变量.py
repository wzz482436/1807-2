from threading import Thread
import time
#多线程对于局部变量不共享
#多线程对于全局变量共享

def show(i):
	num=0
	time.sleep(1)
	num+=1
	print(num)

'''
def show1():
	num=0
	time.sleep(1)
	num+=2
	print(num)
'''	

t = Thread(target=show,args=(3,))
t1 = Thread(target=show,args=(5,))
#t1 = Thread(target=show1,args=(2,))

t.start()
#t1.start()

