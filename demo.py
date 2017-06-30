import urllib2

response = urllib2.urlopen("https://www.baidu.com")
print response.read()
