import urllib
import urllib2

# values = {"usename":"example@email.com","password":"password"}
# data = urllib.urlencode(values)
# url = "https://www.github.com"
# request = urllib2.Request(url,data)
# response = urllib2.urlopen(request )
# print response.read()
 
values = {}
values['username'] = "example@email.com"
values['password'] = "password"
data = urllib.urlencode(values)
url = "https://www.github.com"
geturl = url + "?" + data
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
#print response.read()

print geturl
