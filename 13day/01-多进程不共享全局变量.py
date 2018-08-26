import time 
import os 
num=0 
pid = os.fork()

'''
多进程不共享全局变量
每个进程全局各有一份
'''
if pid == 0:
	time.sleep(3)
	print("子进程")	
	print("子进程%d"%num)

else:
	print("父进程")
	num+=1
	print("父进程%d"%num)



