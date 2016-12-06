#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
 
browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe") # Get local session of firefox
browser.set_page_load_timeout(20)   # 防止页面加载个没完
browser.get('https://www.zhihu.com/')
 
#browser.find_element_by_class_name("js-signin").click()   # 点击登录按钮，一般网站该步可省略
#browser.find_element_by_link_text("登录").click()
browser.find_element_by_xpath("//a[@href='#signin']").click()
email = browser.find_element_by_xpath("//input[@name='account']")
email.clear()
email.send_keys("zuosong_0@163.com")
password = browser.find_element_by_xpath("//input[@name='password']")
password.clear()
password.send_keys("qwertyu")
form = browser.find_element_by_xpath("//form[@class='zu-side-login-box']")
form.submit()
 
somedom = WebDriverWait(browser, 60).until(lambda brow: brow.find_elements_by_class_name("zu-main-feed-con"))[0]
 
html = somedom.find_element_by_xpath("//*").get_attribute("outerHTML")
print html
browser.quit()