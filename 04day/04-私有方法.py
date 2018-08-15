class QQ():
   
    def __openvip(self):
        print("开会员成功")

    def checkqq(self,money):
        if money > 10:
            self.__openvip()
        else:
            print("不能开")
         


qq = QQ()
qq.checkqq(12)
#qq.openvip()

qq1 = QQ()
qq1.checkqq(10)
