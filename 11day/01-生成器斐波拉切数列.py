def fib():
	a,b = 0,1
	for i in range(10):
		#print(b)

		yield b #加上yield就变成生成器格式
		a,b=b,a+b

#print(fib())

G=fib()
#print(next(G)) #这是生成器打印方式最简单普遍的一种

for i in G: #使用循环遍历打印生成器的内容
	print(i)

