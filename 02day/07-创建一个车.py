class Car():

    def __init__(self,color,type):#魔法方法 实例化方法
        self.color = color
        self.type = type
    def __str__(self):#魔法方法
        msg = "颜色是%s,型号是%s"%(self.color,self.type)
        return msg      
    
    def move(self):
        print("车在跑")

    def music(self):
        print("在车里面听音乐")
    
    #def introduce(self):
        #self.move()
        #self.music()
bmw = Car("red","bmwx5")#创建一个车对象
bmw.move()
bmw.music()
#bmw.introduce()
print(bmw)
#bmw.color = "red"
#bmw.type = "bmwx5"

benchi = Car("green","benchi350")
print(benchi)
