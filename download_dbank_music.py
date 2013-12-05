#!/usr/bin/env python
#-*-coding:utf-8-*-'
#Filename:download_file.py

import sys,os
import urllib2
import mimetypes

#url = 'http://blog.longly.me/test.html'
#url = 'http://119.186.162.232/file/MDAwMDAwMDEURf3Tr-CY_qh8r4W5qtfeooOA0cy8M13oIXGNMTY3Qw../91150b6461690cc39e88ae1edb7098c8306ad6b/In%20The%20Tunnels.flac?key=AAABQFKd_QCZV9EO&p=&a=12154662-3af09d6e-48049-0/010100&c=lr:0fc3795e30891d244ed6d1bc261e8967/3072k&mode=download'
url = "http://119.186.162.231/file/MDAwMDAwMDFkE9p_DWds5EypZM-orIhkfYVNYHW_znzjNfgTT69G2w../3f523ca147ad50fce54b26e82be131f44815e1/%E6%A2%A6%E9%87%8C%E6%B0%B4%E4%B9%A1_%E4%BC%B4%E5%A5%8F.mp3?key=AAABQFKd_mnNUsyB&p=&a=12615089-3af09d6e-48049-0/010100&mode=download"
#request = Request(url,{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36"})
url = "http://dl.vmall.com/download/%E6%A2%A6%E9%87%8C%E6%B0%B4%E4%B9%A1_%E4%BC%B4%E5%A5%8F.mp3?f=c0wvztqyyv&i=1&h=1386223185&v=6ee8a3ea&u=98b96cd8&ip=58.240.26.203&p=0&lpid=0&tc=u12615089&auid=12615089&ls="
url = "http://119.186.162.231/file/MDAwMDAwMDFkE9p_DWds5EypZM-orIhkfYVNYHW_znzjNfgTT69G2w../3f523ca147ad50fce54b26e82be131f44815e1/%E6%A2%A6%E9%87%8C%E6%B0%B4%E4%B9%A1_%E4%BC%B4%E5%A5%8F.mp3?key=AAABQFKgK40CLJIt&p=&a=12615089-3af01acb-48049-0/010100&mode=download"
req = urllib2.Request(url)
req.add_header('Referer', 'http://dl.vmall.com/c0wvztqyyv')


urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler({"http":"http://weixianlong:weixianlong@192.168.16.189:8080"})))

f = urllib2.urlopen(req)


html = f.read()

f.info()


f = open("F:/musicdownload/down.mp3","wb")
f.write(html)

f.close()
                                                                                                                    
