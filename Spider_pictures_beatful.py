import urllib2
import re

header = {'User-Aengt':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
request = urllib2.Request(url='http://www.woyaogexing.com/tupian/z/meishi/',headers = header)
req = urllib2.urlopen(request)
buf = req.read()

listurl = re.findall(r'http:.+\.jpg',buf)

i= 0 
for url in listurl :
    f =open (str(i) +'beatful.jpg',"wb")
    req = urllib2.urlopen(url)
    f.write(buf)
    i =i +1
