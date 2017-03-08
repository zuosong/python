#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8

import os.path
import time
import sys,xdrlib
import csv
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

#set the the path of chromedriver.exe
chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
#数据文件存储名称及路径
file_csv='E:\Private Doc\\files\\test.csv'

def csv_reader(file = 'E:\Private Doc\\files\\test.csv'):
    with open(file,'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        url_list = [row['URLs'] for row in reader]
    return url_list

def csv_writer():
    pass

#Use the webdriver to load the page
#input:url,return:browser object
def load_page(url):
    browser = webdriver.Chrome(executable_path=chrome_path) # Get local session of Chrome
    browser.set_page_load_timeout(15)#设置页面加载时间15s
    loadpage=url
    try:
        browser.get(loadpage) # Load page
    except TimeoutException:
        browser.execute_script('window.stop()')
    return browser

#close  the browser
def close_browser(obj):
    browser = obj
    browser.close()

#capture the picture of the page now displaying
#input:browser,the name of pic
def capture_pic(obj,save_fn = "capture.png"):
    browser = obj
    save_pic = save_fn
    browser.save_screenshot(save_pic)

#get the performance the page loading
#input:browser,return:load time(ms)
def get_page_performance(obj):
    browser = obj
    time1 = browser.execute_script("""return window.performance.timing.navigationStart;""")
    time2 = browser.execute_script("""return window.performance.timing.loadEventEnd;""")
    return time2 - time1


#The main function
def main():
    url_list = csv_reader('E:\Private Doc\\files\\test.csv')
    load_time_list = []
    for url in url_list:
        browser = load_page(url)
        load_time_list.append(get_page_performance(browser))
        close_browser(browser)
    print load_time_list


if __name__=="__main__":
    main()
