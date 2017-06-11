import urllib2
req = urllib2.urlopen('https://www.nuomi.com/?cid=002540')
buf = req.read()

import re
listurl = re.findall(r'http:.+\.jpg',buf)
print listurl

i = 0
for url in listurl:
    f = open(str(i)+'.jpg',"wb")
    req = urllib2.urlopen(url)
    f.write(buf)
    i = i+1
