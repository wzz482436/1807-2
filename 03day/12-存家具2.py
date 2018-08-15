class Home():
	
	def __init__(self,area,address,price,hometype):
		self.area = area
		self.address = address
		self.price = price
		self.hometype = hometype
		self.jiaju = []#存放家具
		self.dengs = []#存放灯
 
	def __str__(self):
		msg = "家的面积是%d地址是%s价格是%d万户型是%s"%(self.area,self.address,self.price,self.hometype)
		return msg 
	
	def addBed(self,bed):#加床
		#bed.area = bed.getArea
		if self.area >= bed.getArea():#判断家的面积是否大于加的床的面积，如果大于等于就可以往家里里面加
			self.jiaju.append(bed)
			self.area-=bed.getArea()
			print("加入成功")		
			print(self.area)
		else:
			print("加入失败")

	def addLight(self,light):#加灯
		self.dengs.append(light)

	def switch(self):
		if self.dengs[0].getIsopen():#获取灯是开着还是关着
			self.dengs[0].close()#调用关着
		else:
			self.dengs[0].open()#调用开着
class Bed():
	
	def __init__(self,area,name):
		self.area = area
		self.name = name#品牌
		
	def __str__(self):
		msg = "床的品牌是%s大小是%d"%(self.name,self.area)
		return msg

	def getArea(self):
		return self.area

class Light():
	
	def __init__(self,name):
		self.name = name
		self.isopen = False #默认关灯

	def __str__(self):
		msg = "我叫%s灯"%self.name
		return msg

	def open(self):#开灯
		self.isopen = True
		print("灯亮了")

	def close(self):#关灯
		self.isopen = False
		print("灯灭了")
		
	def getIsopen(self):
		return self.isopen

myHome = Home(120,"北京东城区长安大街666号",1200,"三室二厅")
print(myHome)

ximengsi = Bed(40,"席梦思")
print(ximengsi)

benladeng = Light("本拉登")
print(benladeng)

myHome.addLight(benladeng)

for i in range(10):
	myHome.switch()
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
