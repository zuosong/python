# coding = utf-8
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://www.baidu.com")

print "浏览器最大化"
browser.maximize_window()

browser.quit()

