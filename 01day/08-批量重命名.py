import os
dir = input("请输入文件名字 ")
files = os.listdir(dir)
os.chdir(dir)
print(os.getcwd())

for i in files:
	position = i.rfind(".")
	newname  = i[:position]+"-腾讯"+i[position:]
	os.rename(i,newname)
