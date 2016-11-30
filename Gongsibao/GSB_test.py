#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import sys
import urllib2
#set the the path of chromedriver.exe
chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

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

#get the http_code if there if an error
#Input:page url,return: error code
#def get_httpcode(url):
#    url =url
#    response = urllib2.urlopen(url,timeout=5)
#    return response.getcode()
#    response.close()

#The main function
def main():
    url = raw_input("Please enter you url: ")
    http_code=get_httpcode(url)
    if 200==http_code:
        browser=load_page(url)
        account=raw_input("Please enter your phone number: ")
        passwd=raw_input("Please enter your password: ")
        login_gsb(browser,account,passwd)
        time.sleep(1)
        check_cookies(browser)
        close_browser(browser)
    else:
        print "Please check the url you entered!"



if __name__=="__main__":
    main()
