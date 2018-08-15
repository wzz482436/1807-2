class Person():
    def __init__(self,name):
        self.name = name
    def zhuangzidan(self,dj,zd):#装子弹
        dj.addzidan(zd)#弹夹装子弹
    
    def zhuangdanjia(self,dj,gun):#装弹夹
        gun.addDanJia(dj)#枪自己装弹夹
    
        
class Gun():
    def __init__(self,name):
        self.name = name
        self.dj = None

    def addDanJia(self,dj):
        self.dj = dj

class DanJia():
    def __init__(self,count):
        self.count = count
        self.zds = []#子弹列表
    
    def addzidan(self,zd):#装子弹
        self.zds.append(zd)

class ZiDan():
    def __init__(self,name,sh):
        self.name = name
        self.sh = sh
laowang = Person("老王")
ak47 = Gun("ak47")
dj = DanJia(40)
for i in range(40):
    zd = ZiDan("5.56",5)
    laowang.zhuangzidan(dj,zd)
laowang.zhuangdanjia(dj,ak47)
