class Bank():
    def __init__(self,account,pwd,name):
        self.account = account
        self.__pwd = pwd
        self.name = name

    def getPwd(self):
        return self.__pwd

    def setPwd(self,pwd):
        self.__pwd = pwd 
#---------------------------------------------------
    def __getMoney(self):
        return 100000000

    def check(self,account,pwd):
        if account == self.account and pwd == self.__pwd:
            return self.__getMoney() 
        else:
            print("验证失败")      

bank = Bank("123","123","中国银行")
print(bank.account)
#print(bank.__pwd)
print(bank.getPwd())
print(bank.name)
bank.setPwd("456")
print(bank.getPwd())
print(bank.check("123","456"))
#print(bank.getMoney())
