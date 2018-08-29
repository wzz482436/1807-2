import re
'''
ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print(ret)
'''

s="中国980w平方千米,人口14亿"
print(re.findall(r"\d+",s))

