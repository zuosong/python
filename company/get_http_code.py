#date:2017-2-22
#获取HTTP状态码
#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#Filename:status_code.py

import urllib2

url = raw_input("Please input your url:")
response = None
try:
  response = urllib2.urlopen(url,timeout=5)
except urllib2.URLError as e:
  if hasattr(e, 'code'):
    print 'Error code:',e.code
  elif hasattr(e, 'reason'):
    print 'Reason:',e.reason
finally:
  if response:
    print response.getcode()
    response.close()
