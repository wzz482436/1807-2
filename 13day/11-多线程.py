from threading import Thread
import time

def saysorry():
	print("亲爱的,我一口盐汽水喷死你")
	time.sleep(1)

for i in range(5):
	#t = Thread(target=saysorry)
	#t.start()
	saysorry()
