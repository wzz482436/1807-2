def w1(fun):
	def inner():
		print("-------检查登录-------")
		fun()
	   
	return inner
@w1 #相当于pay = w1(pay) 语法糖
def pay():
	print("-------正在支付-------")

#pay()
#inner=w1(pay)
#inner()

#pay=w1(pay)
pay() #此时装饰器已经装饰完毕
