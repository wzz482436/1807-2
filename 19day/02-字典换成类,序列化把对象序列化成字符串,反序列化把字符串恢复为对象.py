'''
序列化---把对象序列化成字符串
反序列化
'''
import pickle
class StuManger():
    def __init__(self):
        self.list = []
        self.read()
        print(self.list[0].name)
    def save(self):
        name = input("请输入名字")
        age = int(input("请输入年龄"))
        stu = student(name,age)
        self.list.append(stu)
        print(self.list)
        self.writelocation()


    def change(self):
        name = input("请输入名字")
        for p,stu  in enumerate(self.list):
            if stu.name == name:
                newname = input("请输入新的姓名")
                stu.name = newname
                self.list.pop(p)
                self.list.insert(p,stu)
                self.writelocation()
                break

    def writelocation(self):
        f = open("1.data","wb")
        f.write(pickle.dumps(self.list))#序列化
        f.close()

    def read(self):
        f = open("1.data","rb")
        self.list = pickle.loads(f.read())#反序列化
        f.close()

class student():
    def __init__(self,name,age):
        self.name= name
        self.age = age

sm = StuManger()
sm.change()
#sm.save()
