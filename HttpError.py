# !/usr/bin/env python2

import urllib2

request = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(request)
except urllib2.HTTPError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
except urllib2.URLError,e:
    print e.reason
else:
    print 'OK'
