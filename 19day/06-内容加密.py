import hashlib
q= 520
m=hashlib.md5()
m.update(str(q).encode("ascii"))

encodestr = m.hexdigest()
print(encodestr)
