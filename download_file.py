#!/usr/bin/env python
#-*-coding:utf-8-*-'
#Filename:download_file.py

import sys,os
import urllib2
import mimetypes
#import chardet


proxy_handler = urllib2.ProxyHandler({'http': 'http://weixianlong:weixianlong@192.168.16.187:8080/'})
proxy_auth_handler = urllib2.ProxyBasicAuthHandler()

opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
# This time, rather than install the OpenerDirector, we use it directly:
f = opener.open('http://blog.longly.me/test.html')

html = f.read()
html = unicode(html, "UTF-8").encode("GBK")

mt = mimetypes.guess_type(html)
print mt
print html
print f.info()

f = open("E:/musicdownload/down.html","w")
f.write(html)

f.close()
