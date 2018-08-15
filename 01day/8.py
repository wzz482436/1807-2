import os
dir = input("请输入")
files =os.listdir(dir)
os.chdir(dir)
print(os.getcwd())
for i in files:
	x=i.rfind(".")
	newname=i[:x]+"hi"+i[x:]
	os.rename(i,newname)

