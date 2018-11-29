# !usr/bin/env python2
# -coding:utf-8-*
-
import urllib2

request = urllib2.Request('https://www.username.com')
try:
    urllib2.urlopen(request,timeout= 10)
except urllib2.URLError,e:
    print e.reason

