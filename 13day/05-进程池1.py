from multiprocessing import Pool
import os,time,random

def show(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d"%(msg,os.getpid()))
    #random.random()随机生成0~1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f"%(t_stop-t_start))

p=Pool(3) #定义一个进程池，最大进程数3
for i in range(3):
    #Pool.apply_async(要调用的目标,(传递给目标的参数元祖,))
    #每次循环将会用空闲出来的子进程去调用目标
    p.apply_async(show,(i,)) #非阻塞添加进程


print("----start----")
p.close() #关闭进程池，关闭后po不再接收新的请求
p.join() #等待p中所有子进程执行完成，必须放在close语句之后
print("-----end-----")
