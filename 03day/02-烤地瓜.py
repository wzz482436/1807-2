import random
class DiGua():
    def __init__(self):
        self.status = "生的"
        self.times = 0
        self.zl = []#装作料
    def __str__(self):
        msg = "我考的程度是%s"%self.status
        return msg+str(self.zl)
    def cook(self,time):
        self.times+=time
        if self.times >= 1 and self.times <= 2 :
            self.status = "生的"
        elif self.times >= 3 and self.times <= 5:
            self.status = "半生不熟"
        elif self.times >=6 and self.times <= 8:
            self.status = "8分熟"
        elif self.times >= 9 and self.times <= 12:
            self.status = "正好"
        elif self.times > 12:
            self.status = "烤焦了"
        
    def addzl(self,name):
        self.zl.append(name)
        

list = ["盐","糖","番茄酱","黑胡椒","辣椒","孜然"]
digua = DiGua()
for i in range(5):
    digua.cook(random.randint(1,4))
    zl = random.choice(list)
    list.remove(zl)
    digua.addzl(zl)
    print(digua)
'''
digua.cook(1)
print(digua)
digua.cook(2)
print(digua)
digua.cook(2)
print(digua)
digua.cook(3)
print(digua)
digua.cook(4)
print(digua)
'''

