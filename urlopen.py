import urllib2

request = urllib2.Request("https://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()

