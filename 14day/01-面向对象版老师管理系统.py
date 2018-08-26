class menu():
    def __init__(self):
        self.name = "教师管理系统v6.6"
        self.list = []

    def add(self,stu):
        self.list.append(stu)

    def find(self):
        pass

    def delete(self):
        pass

    def get(self):
        pass


class teacher():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
m = menu()
while True:#输入类的对象
    name = input("请输入老师名字")
    age = input("请学生老师年龄")
    sex = input("请输入老师性别")
    stu = teacher(name,age,sex)
    m.add(stu)

