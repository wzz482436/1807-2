class B():
	def __init__(self,name):
		self.name = name
	
	def handle(self):
		print("handle方法1")


class A(B):
	def handle(self):
		print("handle方法2")
		super().handle()


a = A("洲洲")

print(a.name)
a.handle()
