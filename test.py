from urllib2 import Request, urlopen, URLError, HTTPError
import json
posturl = "http://hive.gongsibao.net/api/user/signin"
data= {"username":"YE260","password":"456789"}  
headers = { 'Host': 'hive.gongsibao.net',
			'Connection': 'keep-alive',
			
			'Pragma': 'no-cache',
			'Cache-Control': 'no-cache',
			'Accept': 'application/json, text/plain, */*',
			'Origin': 'http://hive.gongsibao.net',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.22 Safari/537.36',
			'Content-Type': 'application/json;charset=UTF-8',
			'Referer': 'http://hive.gongsibao.net/',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'zh-CN,zh;q=0.8' }  
req = Request(posturl,  json.dumps(data), headers)
try:
    response = urlopen(req)
except HTTPError, e:
    print 'The server couldn\'t fulfill the request.'
    print 'Error code: ', e.code
except URLError, e:
    print 'We failed to reach a server.'
    print 'Reason: ', e.reason
else:
    print 'everything is fine'