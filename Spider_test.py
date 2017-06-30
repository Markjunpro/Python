#!/usr/bin/env python
#-*-coding:utf-8-*-
#from http://blog.csdn.net/iaiti/article/details/49912815
#@Author:iaiti

#test time:2017/5/19/
from imp import reload
import re
import requests
import sys

reload(sys)
circle =  requests.get("http://zone.quanjing.com/share/design/")
ccontent = circle.text
pattern = "(http:[^\s]*?(jpg|png|PNG|JPG))"
finder = re.findall(pattern,circle.text)

truepicture = ".*photo/p0.*"
picpattern = "http:[^\s]*/"
titlepattern = '<p class ="title" title=".*?"'
imgfinder = re.findall(titlepattern,circle.text)
imglen = 0
for n in range(0,len(finder)):
    if re.match(truepicture,finder[n][0]):
        print (finder[n][0])
        
        bigpicture = finder[n][0].replace('photo/p0','photo/r0')
        newimg = request.get(bigpicture)
        temp = imgfinder[imglen].replace('<p class="title" title="','')
        newfinder = re.search(picpattern,finder[n][0])
        temp = "~/python/Spider_img" + temp[0:len(temp)+1]+'.jpg'
        with open(temp,'wb') as newfile:
            newfile.write(newimg.content)

        imglen = imglen +1
