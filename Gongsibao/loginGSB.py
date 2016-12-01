#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe") # Get local session of Chrome
loadpage="http://www.gongsibao.com/login.html"
browser.get(loadpage) # Load page
#assert "公司宝".decode('utf-8') in browser.title

#print browser.title
browser.find_element_by_link_text("登录").click()
time.sleep(2)
user = browser.find_element_by_xpath("//input[@name='username']")
user.clear()
user.send_keys("18618447716")
password = browser.find_element_by_xpath("//input[@name='password']")
password.clear()
password.send_keys("admin111")
time.sleep(1)
form = browser.find_element_by_name("dosubmit")
form.submit()
time.sleep(10)
#try:
    #loginuser = browser.find_element_by_link_text("18618447716")
#    print "Login success!"
#except:
#    print "Failed!"

time.sleep(1)
#browser.get("http://www.gongsibao.com/item/75.html?catid=200")
#time.sleep(3)
#buybtn=browser.find_element_by_xpath("//ul[@id='supplier']/li/div[2]/span[3]").click()
#buybtn.click()
#time.sleep(2)
#cnfrmbtn=browser.find_element_by_class_name("layui-layer-btn0")
#cnfrmbtn.click()
#browser.close()
