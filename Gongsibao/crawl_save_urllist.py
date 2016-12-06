#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cStringIO
import formatter
import urllib
import urlparse
from htmllib import HTMLParser


data = urllib.urlopen("http://www.gongsibao.com/").read()
parser = HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(cStringIO.StringIO())))
parser.feed(data)
parser.close()
url_list= parser.anchorlist
url_update=[]
url_list=list(set(url_list))#排重
for url in url_list:
    parsed = urlparse.urlparse(url)
    host = parsed.netloc.split('@')[-1].split(':')[0]
    if host != 'www.gongsibao.com':
        if host == '' and url.startswith('/'):
            url = 'http://www.gongsibao.com'+url
            url_update.append(url)
        else:
            url_list.remove(url)
    else:
        url_update.append(url)

fl=open('E:\\Private Doc\\files\\test.txt','w')
for i in url_update:
    fl.write(i)
    fl.write("\n")
fl.close()
