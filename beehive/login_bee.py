#!/usr/bin/python  
#encoding:utf-8
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re  
import json

hosturl = 'rd.gongsibao.net' #自己填写  
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）  
posturl = 'http://rd.gongsibao.net/gongsibao-uc/ucuser/loginAjax' #从数据包中分析出，处理post请求的url  


#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。  
headers={'Host':'rd.gongsibao.net',
		'Origin': 'http://rd.gongsibao.net',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
		'Referer': 'http://rd.gongsibao.net/hive/index.html',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		}
#构造Post数据，他也是从抓大的包里分析得出的。  
postData = {"loginName":"123","passwd":"1"}   
  
#需要给Post数据编码  
postData = urllib.urlencode(postData)

  
#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程  
request = urllib2.Request(posturl, postData, headers)  
response = urllib2.urlopen(request)  
cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
html = opener.open(request).read()
if cj:
	print cj
	cj.save('cookiefile.txt')
text = response.read()  
print text


