try:
    age = int(input("请输入年龄"))
except ValueError:
    print("输入有误")


age = input("请输入年龄")
if age.isdigit():
    age = int(age)
else:
    print("输入有误")
