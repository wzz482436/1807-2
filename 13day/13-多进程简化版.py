from multiprocessing import Pool
import time

def show():
	for i in range(3):
		time.sleep(1)
		print("哈哈哈")

p=Pool(3)

for i in range(3):
	time.sleep(1)
	print("呵呵呵")
	p.apply_async(show)

p.close()
#p.join()
