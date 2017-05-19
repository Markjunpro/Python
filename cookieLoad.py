import cookielib
import urllib2

cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard = True,ignore_expires= True)
request = urllib2.Request("https://www.baidu.com")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(request)
print response.read()
