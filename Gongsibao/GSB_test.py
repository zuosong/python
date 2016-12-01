#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import sys,xdrlib
import urllib2
import xlrd
#set the the path of chromedriver.exe
chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
#数据文件存储名称及路径
file_excel='E:\Private Doc\\files\\file.xlsx'
row_start=2#url地址从第2行开始
row_end=17#url地址在第17行结束

#Use the webdriver to load the page
#input:url,return:browser object
def load_page(url):
    browser = webdriver.Chrome(executable_path=chrome_path) # Get local session of Chrome
    loadpage=url
    browser.get(loadpage) # Load page
    return browser

#Find the login button ,enter the account and password to login The website
#Input:the browser,the user account,password;
def login_gsb(obj,account,passwd):
    browser=obj
    browser.find_element_by_link_text("登录").click()
    time.sleep(2)
    user = browser.find_element_by_xpath("//input[@name='username']")
    user.clear()
    user.send_keys(account)
    password = browser.find_element_by_xpath("//input[@name='password']")
    password.clear()
    password.send_keys(passwd)
    time.sleep(1)
    form = browser.find_element_by_name("dosubmit")
    form.submit()

#Check the cookie COOKIE_ACCOUNT_LOGIN_TICKET to confirm if login success
#input browser object;return boolean value:if login success return true
def check_cookies(obj):
    browser= obj
    rtn_log_cookie="return document.cookie.includes('COOKIE_ACCOUNT_LOGIN_TICKET');"
    if_log = browser.execute_script(rtn_log_cookie)
    return if_log

#close  the browser
def close_browser(obj):
    browser = obj
    browser.close()

#capture the picture of the page now displaying
#input:browser,the name of pic
def capture_pic(obj,save_fn="capture.png"):
    browser=obj
    save_pic=save_fn
    browser.save_screenshot(save_pic)

#get the performance the page loading
#input:browser,return:load time(ms)
def get_page_performance(obj):
    browser=obj
    time1=browser.execute_script("""return window.performance.timing.navigationStart;""")
    time2=browser.execute_script("""return window.performance.timing.loadEventEnd;""")
    return time2-time1

def get_url_list(file=file_excel,by_name=u'Sheet1',col_num=6):
    try:
        data = xlrd.open_workbook(file)
        table = data.sheet_by_name(by_name)
        nrows = table.nrows
        ncols = table.ncols
        list = []
        list = table.col_values(col_num)
        return list[row_start:row_end]
    except Exception,e:
        print str(e)

#The main function
def main():
    dict_performance={}
    dict_httpcode={}
    url_list = get_url_list(file_excel,u'Sheet1',6)
    for i in range(len(url_list)):
        response = None
        try:
            response = urllib2.urlopen(url_list[i],timeout=5)
        except urllib2.URLError as e:
            if hasattr(e, 'code'):
                print 'Error code:',e.code
                dict_httpcode[url_list[i]]=e.code
            elif hasattr(e, 'reason'):
                print 'Reason:',e.reason
                dict_httpcode[url_list[i]]=e.reason
        finally:
            if response:
                dict_httpcode[url_list[i]]=response.getcode()
                browser=load_page(url_list[i])
                if check_cookies(browser):
                    #login_gsb(browser,"18618447716","qqqqqqqq")
                #account=raw_input("Please enter your phone number: ")
                #passwd=raw_input("Please enter your password: ")
                #
                loadtime=get_page_performance(browser)
                print "The loadtime of the page is: %d ms " %loadtime
                dict_performance[url_list[i]]=loadtime
                time.sleep(1)
                close_browser(browser)
                response.close()
    print dict_performance
    print dict_httpcode

if __name__=="__main__":
    main()
