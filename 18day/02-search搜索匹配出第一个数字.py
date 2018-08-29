import re

ret = re.search(r"\d+", "阅读次数为 9999")
print(ret.group())
