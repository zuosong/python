#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
"""
利用document.cookie.includes('CompanyPlusAccountUser')判断cookie中是否有标识登录的字段
利用execute_script()执行一段js代码
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe") # Get local session of Chrome
loadpage="http://www.gongsibao.com"
browser.get(loadpage) # Load page
mov = """
    (function () {
      var y = 0;
      var step = 100;
      window.scroll(0, 0);

      function f() {
        if (y < document.body.scrollHeight) {
          y += step;
          window.scroll(0, y);
          setTimeout(f, 50);
        } else {
          window.scroll(0, 0);
          document.title += "scroll-done";
        }
      }

      setTimeout(f, 1000);
    })();
  """
#browser.execute_script(mov)
#assert "公司宝".decode('utf-8') in browser.title

print browser.title
browser.find_element_by_link_text("登录").click()
time.sleep(2)
user = browser.find_element_by_xpath("//input[@name='username']")
user.clear()
user.send_keys("18618447700")
password = browser.find_element_by_xpath("//input[@name='password']")
password.clear()
password.send_keys("qweerr")
time.sleep(1)
form = browser.find_element_by_name("dosubmit")
form.submit()

time.sleep(1)

rtn_log_cookie="return document.cookie.includes('CompanyPlusAccountUser');"
if_log = browser.execute_script(rtn_log_cookie)


if if_log:
    print "Login success!"
else:
    print "Failed!"


browser.close()
