from multiprocessing import Manager,Pool
import time
def writer(q):
	for i in "suyouyoumua":
		q.put(i)
		print("叫老公")
		time.sleep(1)

def reader(q):
	while True:
		if not q.empty():
			msg = q.get()
			print(msg)
			if msg == "a":
				break

			time.sleep(1)
p = Pool(3)
q = Manager().Queue()
p.apply_async(writer,(q,))
p.apply_async(reader,(q,))

#p.apply(writer,(q,))
#p.apply(reader,(q,))

p.close()
p.join()
