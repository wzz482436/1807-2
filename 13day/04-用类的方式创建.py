from multiprocessing import Process
import time

class fun(Process):
	def __init__(self):
		super().__init__()

	def run(self):
		for i in range(5):
			time.sleep(1)
			print("我想带你去网吧里偷耳机")

p = fun()
#p1 = fun() 再给类创建个对象相当于创建个进程,这时会有三个进程,且p和p1进程会同时打印

p.start()
#p1.start()

p.join(3) #等三秒就运行父进程
p.join()
print("再看着你被网管踢")


