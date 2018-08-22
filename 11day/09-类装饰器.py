class Dog(object):
	def __init__(self,fun):
		print("初始化")
		self.__fun = fun

	def __call__(self):
		print("验证")
		self.__fun()
#@Dog相当于 test = Dog(test)
#现在test就是Dog实例对象,如果要执行test()就会去执行Dog里面的call方法
@Dog
def test():
	print("hahah")

test()
