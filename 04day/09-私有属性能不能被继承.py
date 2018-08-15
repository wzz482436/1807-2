class Father():
    def __init__(self,name):
        self.name = name
        self.__sfq = 100

    def __play(self):
        print("玩游戏")

    def getsfq(self):#共有方法
        return self.__sfq

    def Play(self):#共有方法
        self.__play() 
    
class Son(Father):
    pass


son = Son("艾斯")

print(son.name)
#print(son.sfq)#私有不能被直接继承,可以间接继承
print(son.getsfq())
#son.play()#私有方法不能被直接继承,可以间接继承
son.Play()
