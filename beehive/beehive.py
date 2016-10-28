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

hosturl = 'rd.gongsibao.net' # The host url
indexurl= 'http://rd.gongsibao.net/hive/index.html#/app/index'
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据） 

def login():
	name = raw_input('login: ')
	pwd = raw_input('passwd:' )
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
	postData = {"loginName":name,"passwd":pwd}   

	#需要给Post数据编码  
	postData = urllib.urlencode(postData)

	#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程    
	request = urllib2.Request(posturl, postData, headers)  
	response = urllib2.urlopen(request)  
	cj = cookielib.LWPCookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	urllib2.install_opener(opener)
	html = opener.open(request).read()

def createOrder():
	login()
	postData = {"prodList":[{"originCount":5498,"presentCount":3498,"areaStr":"北京市-北京市-朝阳区","productIdStr":"1nR-2w~~","productName":"内资公司注册","cityIdStr":"1nR72ty9EVJV","itemList":[{"pkid":146645,"serviceId":4348,"cityId":101110105,"priceAuditId":175087,"originalPrice":0,"price":0,"cost":0,"isMust":1,"stock":-1,"isOnSale":1,"addTime":"2016-06-30 18:22:04","addUserId":2158,"remark":"","unitId":2026,"agentId":"","agentName":"","propertyName":"信息科技","propertyId":20774,"typeName":"服务费","typeId":203178,"unitName":"次","priceIdStr":"1nB83dm4","pkidStr":"1nB83dm4","check":1,"originalPriceTem":0,"priceTem":0},{"pkid":146646,"serviceId":4349,"cityId":101110105,"priceAuditId":175087,"originalPrice":49800,"price":49800,"cost":0,"isMust":1,"stock":-1,"isOnSale":1,"addTime":"2016-06-30 18:22:04","addUserId":2158,"remark":"","unitId":2027,"agentId":"","agentName":"","propertyName":"信息科技","propertyId":20774,"typeName":"工本费","typeId":203179,"unitName":"件","priceIdStr":"1nB83dm7","pkidStr":"1nB83dm7","check":1,"originalPriceTem":498,"priceTem":498},{"pkid":146647,"serviceId":4350,"cityId":101110105,"priceAuditId":175087,"originalPrice":500000,"price":300000,"cost":0,"isMust":0,"stock":-1,"isOnSale":1,"addTime":"2016-06-30 18:22:04","addUserId":2158,"remark":"","unitId":2024,"agentId":"","agentName":"","propertyName":"信息科技","propertyId":20774,"typeName":"地址费","typeId":203180,"unitName":"年","priceIdStr":"1nB83dm6","pkidStr":"1nB83dm6","originalPriceTem":5000,"priceTem":3000,"check":1}],"check":1,"price":0}],"payablePrice":3498,"orderDiscount":"","sourceTypeId":3045,"accountMobile":18618447711}
	postData = json.dumps(postData,separators=(',',':'))
	posturl = 'http://rd.gongsibao.net/gongsibao-order/api/order/create'
	headers={'Host':'rd.gongsibao.net',
		'Origin': 'http://rd.gongsibao.net',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
		'Referer': 'http://rd.gongsibao.net/hive/index.html',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Content-Type': 'application/json;charset=UTF-8'
		}
	request = urllib2.Request(posturl, postData, headers)  
	response= urllib2.urlopen(request)  
	text = response.read()  
	print unicode(text)


def getAllOrder():
	login()
	allOrderUrl = 'http://rd.gongsibao.net/gongsibao-order/api/order/list?currentPage=1&pageSize=10'
	req = urllib2.Request(allOrderUrl)
	#print req
	res_data = urllib2.urlopen(req)
	page = res_data.read()
	#page = json.dumps(page,indent = 4)
	print page
	file = open('page.txt','w')
	file.write(page)
	file.close 

def getInfo():
	login()
	curUrl = 'http://rd.gongsibao.net/gongsibao-uc/ucuser/currentInfo'
	req = urllib2.Request(curUrl)
	user_data = urllib2.urlopen(req)
	userInfo = user_data.read()
	print userInfo

def getFunction():
	login()
	curUrl = raw_input('输入链接地址：')
	req = urllib2.Request(curUrl)
	user_data = urllib2.urlopen(req)
	userInfo = user_data.read()
	print userInfo


#createOrder()
#getAllOrder()
getFunction()