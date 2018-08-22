year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))

months = [0,31,59,90,120,151,181,212,243,273,304] # months累加记录1-11月的总天数

if 0 < month < 12:   # 假设为非闰年时，当前日期的天数
    sum = months[month - 1] + day

flag = 0
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):   # 判断是否为闰年，如果为闰年flag = 1
    flag = 1

if flag == 1 and month > 2:  # 年份为闰年且月份大于2
    sum += 1

print("%d.%d.%d 是 %d 年的第 %d 天" % (year,month,day,year,sum))
