class Person():
    def __init__(self,name):
        self.name = name

class Gun():
    def __init__(self,name):
        self.name = name

class DanJia():
    def __init__(self,count):
        self.count = count

class ZiDan():
    def __init__(self,name,sh):
        self.name = name
        self.sh = sh
laowang = Person("老王")
ak47 = Gun("ak47")
dj = DanJia(40)
for i in range(40):
    zd = ZiDan("5.56",5)


