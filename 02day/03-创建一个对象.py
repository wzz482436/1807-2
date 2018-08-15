class Car:
    #有行为的类
    def run(self):
        print("跑")
    def turn(self):
        print("转向")


mashaladi = Car()#通过汽车类创建出一个mashaladi的对象
mashaladi.run()#目前不需要传参数
mashaladi.turn()#目前不需要传参数


class BingXiang:
    
    def openDoor(self):
        print("开门")

    def zhuangdaxiang(self):
        print("装大象")

    def closeDoor(self):
        print("关门")

ximenzi = BingXiang()
ximenzi.openDoor()
ximenzi.zhuangdaxiang()
ximenzi.closeDoor()
    
