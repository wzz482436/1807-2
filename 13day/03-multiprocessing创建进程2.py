from multiprocessing import Process
import time

def show(name):
	for i in range(10):
		time.sleep(1)
		print(name)

p = Process(target = show,args=("放羊",))
p.start() #启动进程

#p.join() #等待子进程结束再运行父进程
#p.join(3) #最多等三秒

time.sleep(2)
p.terminate() #不管子进程结束没结束,都让子进程停止

for i in range(10):
	print("嫖娼")  #属于父进程
