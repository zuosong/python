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
indexurl= 'http://rd.gongsibao.net/hive/index.html#/app/index'
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）  
post_login_url = 'http://rd.gongsibao.net/gongsibao-uc/ucuser/loginAjax' #从数据包中分析出，处理post请求的url  
post_create_url = 'http://rd.gongsibao.net/gongsibao-order/api/order/create' #从数据包中分析出，处理post请求的url  

#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。  
headers={'Host':'rd.gongsibao.net',
		'Origin': 'http://rd.gongsibao.net',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
		'Referer': 'http://rd.gongsibao.net/hive/index.html',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.8'
		}
#构造Post数据，他也是从抓大的包里分析得出的。
post_login_Data ={"loginName":"18618447716","passwd":"fqwwewrw"}
post_order_Data = {"prodList":[{"originCount":5498,"presentCount":5498,"areaStr":"北京市-北京市-朝阳区","productIdStr":"1nR-2w~~","productName":"内资公司注册","cityIdStr":"1nR72ty9EVJV","itemList":[{"pkid":146645,"serviceId":4348,"cityId":101110105,"priceAuditId":175087,"originalPrice":0,"price":0,"cost":0,"isMust":1,"stock":-1,"isOnSale":1,"addTime":"2016-06-30 18:22:04","addUserId":2158,"remark":"","unitId":2026,"agentId":"","agentName":"","propertyName":"信息科技","propertyId":20774,"typeName":"服务费","typeId":203178,"unitName":"次","priceIdStr":"1nB83dm4","pkidStr":"1nB83dm4","check":1,"originalPriceTem":0,"priceTem":0},{"pkid":146646,"serviceId":4349,"cityId":101110105,"priceAuditId":175087,"originalPrice":49800,"price":49800,"cost":0,"isMust":1,"stock":-1,"isOnSale":1,"addTime":"2016-06-30 18:22:04","addUserId":2158,"remark":"","unitId":2027,"agentId":"","agentName":"","propertyName":"信息科技","propertyId":20774,"typeName":"工本费","typeId":203179,"unitName":"件","priceIdStr":"1nB83dm7","pkidStr":"1nB83dm7","check":1,"originalPriceTem":498,"priceTem":498},{"pkid":146647,"serviceId":4350,"cityId":101110105,"priceAuditId":175087,"originalPrice":500000,"price":500000,"cost":0,"isMust":0,"stock":-1,"isOnSale":1,"addTime":"2016-06-30 18:22:04","addUserId":2158,"remark":"","unitId":2024,"agentId":"","agentName":"","propertyName":"信息科技","propertyId":20774,"typeName":"地址费","typeId":203180,"unitName":"年","priceIdStr":"1nB83dm6","pkidStr":"1nB83dm6","originalPriceTem":5000,"priceTem":5000,"check":1}],"check":1,"price":0}],"payablePrice":5498,"orderDiscount":"","sourceTypeId":3045,"accountMobile":18618440099}
  
#需要给Post数据编码  
post_login_Data = urllib.urlencode(post_login_Data)
post_order_Data = json.dumps(post_order_Data,separators=(',',':'))  

  
#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程  
request_login = urllib2.Request(post_login_url, post_login_Data, headers)  
response_login = urllib2.urlopen(request_login)  


#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie  
cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)

html = opener.open(request_login).read()
if cj:
	print cj
	cj.save('cookiefile.txt')
text = response_login.read()  
print text


headers_new={'Host':'rd.gongsibao.net',
		'Origin': 'http://rd.gongsibao.net',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
		'Referer': 'http://rd.gongsibao.net/hive/index.html',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Content-Type': 'application/json;charset=UTF-8'
		}


#打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）  
h = urllib2.urlopen(indexurl)  
#发送创建订单post数据
request_create = urllib2.Request(post_create_url, post_order_Data, headers_new)  
response_create = urllib2.urlopen(request_create)  
text = response_create.read()  
print text
