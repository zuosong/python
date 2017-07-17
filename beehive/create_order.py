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
posturl = 'http://rd.gongsibao.net/gongsibao-order/api/order/create' #从数据包中分析出，处理post请求的url  

#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。  
headers={'Host':'rd.gongsibao.net',
		'Connection': 'keep-alive',
		'Pragma': 'no-cache',
		'Cache-Control': 'no-cache',
		'Accept': 'application/json, text/plain, */*',
		'Origin': 'http://rd.gongsibao.net',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
		'Content-Type': 'application/json;charset=UTF-8',
		'Referer': 'http://rd.gongsibao.net/hive/index.html',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Cookie':'COOKIE_LOGIN_TICKET=2c0df147-0481-472a-94c0-d925067fe929; COOKIE_LOGIN_TICKET=2c0df147-0481-472a-94c0-d925067fe929'
		}
#构造Post数据，他也是从抓大的包里分析得出的。  
postData = {"prodList":[{"originCount":5000,"presentCount":5000,"areaStr":"北京市-北京市-朝阳区","productIdStr":"0nY~","productName":"集团公司注册","cityIdStr":"1nR72ty9EVJV","itemList":[{"pkid":3585,"serviceId":289,"cityId":101110105,"priceAuditId":89,"originalPrice":500000,"price":500000,"cost":0,"isMust":1,"stock":0,"isOnSale":1,"addTime":"2016-06-21 11:11:23","addUserId":1,"remark":"","unitId":2022,"agentId":"","agentName":"","propertyName":"科技类","propertyId":2073,"typeName":"服务费","typeId":2032,"priceIdStr":"1HFy3g~~","unitName":"件","pkidStr":"1HFy3g~~","check":1,"originalPriceTem":5000,"priceTem":5000}],"check":1,"price":0}],"payablePrice":5000,"orderDiscount":"","accountMobile":123}
  
#需要给Post数据编码  
postData = json.dumps(postData,separators=(',',':'))  

  
#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程  
request = urllib2.Request(posturl, postData, headers)  
response = urllib2.urlopen(request)  
text = response.read()  
print text
