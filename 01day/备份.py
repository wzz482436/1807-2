name = input("请输入备份文件名字 ")
f = open(name,"r")
wzz = f.read()

f1 = open("备份.txt","w")
f1.write(wzz)

f.close()
f1.close()
