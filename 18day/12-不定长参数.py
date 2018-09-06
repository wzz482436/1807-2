def test(a,b,d):
    c = a+b+d
    print(c)

#test(1,2,3)

#不定长参数的写法
def test(a,*args,b=12,**kwargs):
    #print(a)
    #print(b)
    #print(args)
    #print(kwargs)
    sum = 0#局部变量
    sum = sum+a
    for i in args:
        sum = sum+i
    sum =sum+b
    for v in kwargs.values():
        sum = sum+v
    return sum
ret = test(1,2,3,4,5,b=20,m=12,n=22)
print(ret)
