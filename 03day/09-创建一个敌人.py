class Person():
    def __init__(self,name):
        self.name = name
        self.gun = None#刚初始化人对象没有枪
    def zhuangzidan(self,dj,zd):#装子弹
        dj.addzidan(zd)#弹夹装子弹
    
    def zhuangdanjia(self,dj,gun):#装弹夹
        gun.addDanJia(dj)#枪自己装弹夹
   
    def naqiang(self,gun):#拿枪
        self.gun = gun 
        
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
laowang = Person("老王")#创建一个老王对象
ak47 = Gun("ak47")#创建枪对象
dj = DanJia(40)#创建一个弹夹
for i in range(40):#创建一些子弹
    zd = ZiDan("5.56",5)
    laowang.zhuangzidan(dj,zd)#老王装子弹
laowang.zhuangdanjia(dj,ak47)#老王装弹夹
laowang.naqiang(ak47)#老王拿枪
laosong = Person("老宋")#创建一个敌人
