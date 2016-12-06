#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cStringIO
import formatter
import urllib
from htmllib import HTMLParser


data = urllib.urlopen("http://www.gongsibao.com").read()
parser = HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(cStringIO.StringIO())))
parser.feed(data)
parser.close()
url_list= parser.anchorlist
fl=open('E:\\Private Doc\\files\\test.txt','w')
for i in url_list:
    fl.write(i)
    fl.write("\n")
fl.close()
