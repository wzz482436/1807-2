from threading import Thread
import time

def sing():
	for i in range(10):
		print("啦啦啦")
		time.sleep(1)
def dance():
	for i in range(10):
		print("蹦迪")
		time.sleep(1)

t1 = Thread(target=sing)
t2 = Thread(target=dance)
t1.start()
t2.start()
t1.join(1) #t1进程最多等一秒就执行主线程
t2.join(1) #t2进程最多等一秒就执行主线程,这样写相当于等两秒就执行主线程
print("儿子儿子我是你爸爸") #主线程
