#!/usr/bin/env python
#-*- coding: utf-8 -*-
#modified date : 2017-2-22

import xdrlib,sys
import xlrd
import time
import urllib2
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

#打开一个指定的Excel文件；输入:文件名；返回：文件对象
def open_excel(file='E:\Private Doc\\files\\file.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

#根据索引获取Excel表格中的数据，返回一个数据list.参数：file：excel件路径，colnameindex:表头列名所在行的索引，by_index:表的索引
def excel_table_byindex(file = 'E:\Private Doc\\files\\file.xlsx', colnameindex = 0, by_index = 0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    ncols = table.ncols
    colnames = table.row_values(colnameindex)
    list = []
    for rownum in range(0,nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[1]] = row[1]
            list.append(app)
    return list


#根据名称获取Excel表格中的数据，返回一个数据list.参数：file:Excel路径，colnameindex表头列名所在行的索引，by_name:sheet1名称
def excel_table_byname(file = 'E:\Private Doc\\files\\file.xlsx', colnameindex = 0, by_name = u'Sheet2'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows
    colnames = table.row_values(colnameindex)
    list = []
    for rownum in range(0,nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list

#获取指定一列的值,返回数据list.参数：file，Excel文件路径；index，指定列所在的tab index;col_num：列数
def excel_table_col_I(file = 'E:\Private Doc\\files\\file.xlsx',by_index = 1,col_num = 1):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    ncols = table.ncols
    list = []
    list = table.col_values(col_num)
    return list

#打开指定的url地址，并且返回加载时间(ms).输入参数：url地址；返回：null
def open_url_get_performance(url):
    Chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    browser = webdriver.Chrome(executable_path = Chrome_path) # Get local
    browser.get(url)
 #   if_in = if_login(browser)
 #   if if_in:
 #       print "The url %s has login !" %url
 #   else:
 #       login_page(browser)
 #       print "Now the url %s login!" %url
    Load_time = get_page_performance(browser)
    print "The page %s load time is %d ms" %(url,Load_time)
    time.sleep(1)
    browser.close()

#获取页面的加载时间(ms),输入参数：浏览器对象；返回：页面加载时间(ms)
def get_page_performance(obj):
    browser = obj
    time_start = browser.execute_script("""return window.performance.timing.navigationStart;""")
    time_end = browser.execute_script("""return window.performance.timing.loadEventEnd;""")
    return time_end - time_start

#获取打开的页面的状态码，输入参数：url地址。返回:空
def get_status_code(url):
    try:
        response = urllib2.urlopen(url, timeout=5)
    except urllib2.URLError as e:
        if hasattr(e, 'code'):
            print 'The url',url,'retrun Error code:',e.code
        elif hasattr(e, 'reason'):
            print 'Reason:',e.reason
    finally:
        if response:
            #print 'The url',url,'Code: ',response.getcode()
            response.close()

#根据页面的cookie值判断是否登录成功，输入参数：浏览器对象；返回：true/false;
def if_login(obj):
    browser = obj
    rtn_log_cookie="return document.cookie.includes('CompanyPlusAccountUser')"
    if_log = browser.execute_script(rtn_log_cookie)
    return if_log

#进行登录操作,输入参数：浏览器对象,返回null
def login_page(obj):
    browser = obj
    browser.find_element_by_link_text("登录").click()
    time.sleep(2)
    user = browser.find_element_by_xpath("//input[@name='username']")
    user.clear()
    user.send_keys("18618447700")
    password = browser.find_element_by_xpath("//input[@name='password']")
    password.clear()
    password.send_keys("QWERTY")
    time.sleep(1)
    form = browser.find_element_by_name("dosubmit")
    form.submit()

def main():
    #tables = excel_table_byindex()
    #for row in tables:
    #    print row

    #tables = excel_table_byname()
    #for row in tables:
    #    print row
    tables = excel_table_col_I('E:\Private Doc\\files\\file.xlsx',0,6)
    print "There are %d url links in the table." % (len(tables)-2)
    for i in range(2,len(tables)):
    #    print tables[i]
        open_url_get_performance(tables[i])
        #get_status_code(tables[i])
    #url="http://www.gongsibao.com"
    #open_url_get_performance(url)

if __name__=="__main__":
    main()
