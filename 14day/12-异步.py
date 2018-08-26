from multiprocessing import Pool
import time

def download():
	for i in range(10):
		#print("已下载%d%%"%(i*10))
		time.sleep(1)
	return "下载完成"

def noti(args):
	print(args)

p=Pool()
p.apply_async(download,callback=noti)
#callback告诉线程,你下载完成通过noti函数告诉我
#同步: 看着他下载完
#异步: 他下载,你去干别的,下载完告诉你
p.close()

for i in range(20):
	print("吃饭睡觉打豆豆")
	time.sleep(1)
