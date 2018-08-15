class Manger():
    def __init__(self):
        self.name = "学生管理大师v1.0"
        self.list = []

    def add(self,stu):
        self.list.append(stu)

    def find(self):
        pass

    def delete(self):
        pass

    def change(self):
        pass


class Student():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
m = Manger()
while True:#输入类的对象
    name = input("请输入学生名字")
    age = input("请学生学生年龄")
    sex = input("请输入学生性别")
    stu = Student(name,age,sex)
    m.add(stu)
    
