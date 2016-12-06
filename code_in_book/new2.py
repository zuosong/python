# coding = utf-8
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://www.baidu.com")

print "设置浏览器宽480、高800显示"
browser.set_window_size(480,800)

browser.quit()

