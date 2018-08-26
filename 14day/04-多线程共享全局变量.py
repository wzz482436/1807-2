from threading import Thread
import time

num = 100
def work1():

	for i in range(100):
		num += 1
print("哈哈")
time.sleep(2)

def work2():
	global num
        
	for i in range(100):
		num +=1
print("%d"%num)
time.sleep(5)


t1 = Thread(target=work1)
t1.start()


t2 = Thread(target=work2)
t2.start()
