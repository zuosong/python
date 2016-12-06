#!coding:utf-8    相信这句大家都懂的，不解释

#导入需要的python模块httplib，用来模拟提交http请求，详细的用法可见python帮助手册

import httplib

#导入需要的python模块urllib，用来对数据进行编码
import urllib
#定义请求头

reqheaders={'Referer' : 'http://devehive.gongsibao.net/',
'Origin':'http://devehive.gongsibao.net',
'Referer':'http://devehive.gongsibao.net',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',}

#定义post的参数

reqdata={"username":"KG298","password":"012345"}

#对请求参数进行编码

data=urllib.urlencode(reqdata)

#利用httplib库模拟接口请求

#先连接到人人

conn=httplib.HTTPConnection('devehive.gongsibao.net')

#提交登录的post请求
conn.request('POST', '/api/user/signin', data, reqheaders)

#获取服务器的返回
res=conn.getresponse()

#打印服务器返回的状态
print(res.status)

#以dictionary形式答应服务器返回的 response header

#print(res.msg)
#打印服务器返回请求头中设置的cookie
#print(res.getheader('Set-Cookie'))
