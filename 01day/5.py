import os
dir = input("请输入")
files= os.listdir(dir)
os.chdir(dir)
print(os.getcwd())
for i in files:
	position = i.rfind(".")
	newname = i[:position]+"baby"+i[position:]
	os.rename(i,newname)
