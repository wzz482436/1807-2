class Game():
    count = 3#3个英雄  战士 法师 道士
    def __init__(self,name):#魔法方法
        self.name = name

    def play(self):#实例方法
        print("大家一起玩")

    @classmethod
    def getCount(cls):
        return cls.count

    @staticmethod
    def print_menu():
        print("1、开始游戏")
        print("2、结束游戏")

cq = Game("传奇")

print(cq.name)#调用实例属性
cq.play()#调用实例方法

print(Game.count)#调用类属性
Game.getCount()#通过类调用类方法
cq.getCount()#通过实例调用类方法

Game.print_menu()#通过类调用静态方法
cq.print_menu()#通过实例调用静态方法




    
