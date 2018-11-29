# !/usr/bin/env python3

import urllib
import urllib2

url = "https://www.github.com"
user_agent='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Mobile Safari/537.36'
values = {'username':'example@email.com','password':'example_password'}
headers = {'User-agent':user_agent,'Referer':'https://www.github.com'}
data = urllib.urlencode(values)
request =urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
page = response.read()

print("Page:\n",page)
