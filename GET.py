import urllib2
import urllib

values = {}
values['username']= "example@email.com"
values['password'] = "ecample_password"  
data = urllib.urlencode(values) # encoding
url = "https://www.github.com"   
geturl = url + '?' + data   # login url, equivalent POST data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)


print("url:", geturl)
print("response text:\n",response.read()[:500])
