#!/usr/bin/env python
#data:2017-2-22
#脚本：测试页面加载时间
from selenium import webdriver
import time
browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
loadpage="http://www.gongsibao.com"
browser.get(loadpage) # Load page
time1=browser.execute_script("""return window.performance.timing.navigationStart;""")
time2=browser.execute_script("""return window.performance.timing.loadEventEnd;""")
print time2-time1
