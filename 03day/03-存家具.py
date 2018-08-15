import random
class Home():
    def __init__(self,area,type,address):
        self.area = area
        self.type = type
        self.address = address
        self.jiaju = []#家具列表
    def __str__(self):
        msg = "面积是%d,户型是%s,地址是%s,家具有%d个"%(self.area,self.type,self.address,len(self.jiaju))
        return msg

    def add(self,jj):#添加家具的功能
        self.jiaju.append(jj)
        
    def tell_area(self):#告诉主人剩余多少面积的功能
        all_a = 0
        for i in self.jiaju:
            all_a+=i.area
        diff = self.area - all_a
        return diff

class Bed():
    def __init__(self,area,name):
        self.area = area
        self.name = name
home = Home(540,"四合院","北京长安街")
for i in range(100):
    bed = Bed(random.randint(8,12),"席梦思")
    if home.tell_area() < bed.area:
        break
    home.add(bed)
print(home)
