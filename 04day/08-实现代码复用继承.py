class Animal():
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("吃")

    def sleep(self):
        print("睡")

class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Pig(Animal):
    pass

bsm = Cat("波斯猫")
bsm.eat()
bsm.sleep()
print(bsm.name)

wc = Dog("旺财")
wc.eat()
wc.sleep()
print(wc.name)

pq = Pig("佩奇")
pq.eat()
pq.sleep()
print(pq.name)


