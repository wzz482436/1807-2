from threading import Thread
import time
class MyThread(Thread):
    def run(self): #必须是run
        for i in range(10):
            print("哈哈哈",self.name)
            time.sleep(1)



t = MyThread()
t.start()
t1 = MyThread()
t1.start()
