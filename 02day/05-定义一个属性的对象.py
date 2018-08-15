class Person:
    def eat(self):
        print("吃饭")
    def sleep(self):
        print("睡觉")
    def play(self):
        print("玩")
    def introduce(self):
        print("我年龄是%d 我的身高是%d"%(self.age,self.height))


zhangzihao = Person()
zhangzihao.eat()
zhangzihao.sleep()
zhangzihao.play()
zhangzihao.age = 19#添加属性
zhangzihao.height = 178#添加属性
zhangzihao.introduce()
print(zhangzihao.age)
print(zhangzihao.height)


ln = Person()
ln.eat()
ln.sleep()
ln.play()
ln.age = 20#添加属性
ln.height = 180
ln.introduce()


