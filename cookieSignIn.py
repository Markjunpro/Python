# !usr/bin/env python2
# -coding:utf-8-*-


import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
cookie =cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
    'username':'example_username',
    'email':'example@email.com',
    'password':'example_password'
    })
loginUrl = 'https://www.github.com'
result = opener.open(loginUrl,postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
gradeUrl = 'https://www.github.com'
result = opener.open(gradeUrl)
print result.read()

