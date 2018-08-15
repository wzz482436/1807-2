class CardMan():
    def __init__(self):
        self.cards = []

    def insert(self):
        d = {}
        name = input("请输入姓名")
        age = input("请输入年龄")
        d["name"] = name
        d["age"] = age
        self.cards.append(d)
        self.save()
  
    def menu(self):
        self.open()#读取
        while True:
            num = int(input("请选择功能 1、添加 2、查看"))
            if num == 1:
                self.insert()

    def save(self):
        with open("data.data","w") as f:
            f.write(str(self.cards))

    def open(self):
        f = open("data.data","r")
        self.cards = eval(f.read())
        #if len(f.read()) != 0:
           #self.cards = eval(f.read())
        #    print(f.read())


cm = CardMan()
cm.menu()
