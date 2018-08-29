import re
url = "https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg,https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg"

#print(re.search(r"https://.+\.jpg",url))

print(re.search(r"https://.+?\.jpg",url)) #加?把贪婪模式变成非贪婪
