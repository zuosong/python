﻿#!usr/bin/python
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

#browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe") # Get local session of firefox
browser = webdriver.Firefox()
browser.get("https://www.baidu.com/") # Load page
assert "百度一下，你就知道".decode('utf-8') in browser.title

print browser.title

browser.close()
