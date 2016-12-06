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

hosturl = 'http://testhive.gongsibao.net' #自己填写  
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）  
posturl = 'http://testhive.gongsibao.net/api/user/signin' #从数据包中分析出，处理post请求的url  
  
#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie  
cj = cookielib.CookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)  
  
#打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）  
h = urllib2.urlopen(hosturl)  
  
#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。  
headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.22 Safari/537.36',  
			'Referer' : 'http://testhive.gongsibao.net/login.html',
			'Accept': 'application/json, text/plain, */*'
		}  
#构造Post数据，他也是从抓大的包里分析得出的。  
postData = {"username":"北分2","password":"gongsibao717"}  
  
#需要给Post数据编码  
postData = json.dumps(postData,ensure_ascii=False)  

  
#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程  
request = urllib2.Request(posturl, postData, headers)  
#print dir(request)  
#print request.get_host()
#print request.get_data()
#print request.get_full_url()
response = urllib2.urlopen(request)  
text = response.read()  
print text
