def w1(fun):
	def inner(*args,**kwargs):
		print("-----检查登录中----")
		ret =  fun(*args,**kwargs)
		return ret
	return inner


#无参无返回值
@w1
def test1():
	print("哈哈哈")

#无参有返回值
@w1
def test2():
	return "嘎嘎嘎"

#有参无返回值
@w1
def test3(a,b):
	print("呵呵呵")

#有参有返回值
@w1
def test4(a,b):
	print("%d+%d=%d"%(a,b,a+b))
	return "老王"

test1()
print(test2())
test3(1,2)
print(test4(1,2))
