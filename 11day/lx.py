def w1(fun):
	def inner():
		print("装饰中")
		fun()
	return inner
@w1
def show():
	print("装饰完毕")

show()
