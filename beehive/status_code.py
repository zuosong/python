#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#Filename:states_code.py

import sys

import urllib2
from time import sleep

f = open("page1.txt","r")
file = open("out1.txt","w+")
savedStdout = sys.stdout #保存标准输出流
sys.stdout = file #标准输出重定向至文件
urlList = f.readlines()
response = None
for url in urlList:
    #print url
    try:
      response = urllib2.urlopen(url,timeout=5)
    except urllib2.URLError as e:
      if hasattr(e, 'code'):
        print 'The url',url,'retrun Error code:',e.code
      elif hasattr(e, 'reason'):
        print 'Reason:',e.reason
    finally:
      if response:
        print 'The url',url,'Code: ',response.getcode()
        response.close()

sys.stdout = savedStdout #恢复标准输出流
print 'This message is for screen!'