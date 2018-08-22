'''
def test1():
	print("--- in test1 func----")

#调用函数
test1()

#引用函数
ret = test1

print(id(ret))
print(id(test1))

#通过引用调用函数
ret()
'''

def show(num):
	def show1(a,b):
		return a+b+num
	return show1
x=show(1)
print(x(1,2))
