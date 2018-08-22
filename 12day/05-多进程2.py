import os

a = os.fork()

if a == 0:
    print('子进程是%d,父进程是%d'%(os.getpid(),os.getppid())) #pid是进程号

else:
    print('父进程%d,子进程%d'%(os.getpid(),a))
print('父子都可以执行代码')
