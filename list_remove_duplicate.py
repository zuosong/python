#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Different methods to remove the duplicated urls in list"""
import cStringIO
import formatter
import urllib
import urlparse
from htmllib import HTMLParser

def get_htmlsource(url):
    data = urllib.urlopen(url).read()
    parser = HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(cStringIO.StringIO())))
    parser.feed(data)
    parser.close()
    url_list= parser.anchorlist
    return url_list

def main():
    url_list=get_htmlsource("http://www.gongsibao.com")
    url_list.sort()
    #method 1
    #url_update=list(set(url_list))#排重
    #url_update.sort()
    #method 2
    url_update= []
    for k in url_list:
        if k not in url_update:
            url_update.append(k)

    file_order=open('E:\\Private Doc\\files\\test1.txt','w')
    for i in url_list:
        file_order.write(i)
        file_order.write("\n")
    file_order.close()
    file_unorder=open('E:\\Private Doc\\files\\test2.txt','w')
    for j in url_update:
        file_unorder.write(j)
        file_unorder.write("\n")
    file_unorder.close()

if __name__ == '__main__':
    main()
