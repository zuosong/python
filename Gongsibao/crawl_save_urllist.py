#!/usr/bin/env python
# -*- coding: utf-8 -*-
#date 2016-12-7
#author zuosong
#fixed point :move the code into functions
import cStringIO
import formatter
import urllib
import urlparse
from htmllib import HTMLParser

def get_urls(url):
    data = urllib.urlopen(url).read()
    parser = HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(cStringIO.StringIO())))
    parser.feed(data)
    parser.close()
    url_list= parser.anchorlist
    return url_list

def url_filter(url):
    url_list=get_urls(url)
    url_list=list(set(url_list))#排重
    url_list.sort()#进行一次排序
    url_update = []
    print len(url_list)
    for url in url_list:
        parsed = urlparse.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        if host != 'www.gongsibao.com':
            if host == '' and url.startswith('/'):
                url = 'http://www.gongsibao.com'+url
                url_update.append(url)
                #print url
            else:
                url_list.remove(url)
                #print url
        else:
            url_update.append(url)
            #print url
    print '**********'
    return url_update

def output_urllist(file='E:\\Private Doc\\files\\test.txt',url_list=[]):
    fl=open(file,'w')
    url_update = url_list
    print len(url_update)
    for i in url_update:
        fl.write(i)
        fl.write("\n")
    fl.close()

def main():
    #url_list=url_filter('http://www.gongsibao.com/')
    url_list = ['http://www.gongsibao.com/ask_149/8.html',]
    for url in url_list:
        url_new_list = []
        url_new_list = url_filter(url)
        url_list.extend(url_new_list)
        url_list=list(set(url_list))#排重
    output_urllist('E:\\Private Doc\\files\\test.txt',url_list)

if __name__ =='__main__':
    main()
