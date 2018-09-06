from multiprocessing import Pool
import time

def show():
	for i in range(10):
		time.sleep(1)
		print("哈哈哈")

p=Pool(3) #创建一个进程池,可以装无限个进程,加上参数比如3,只能执行3个进程
for i in range(3):
	p.apply_async(show) #非阻塞添加进程,三个进程同时进行

	#p.apply(show) #阻塞添加进程,30遍的任务,三个进程依次执行10遍
	print("添加成功")

p.close() #关闭进程池

p.join() #如果不加join,不等待子进程运行结束,三个子进程只会同时运行一遍就会运行父进程,父进程运行完 代码就结束

print("啦啦啦")
