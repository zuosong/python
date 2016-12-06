import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

iedriver = "C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe"
os.environ["webdriver.ie.driver"] = iedriver

driver = webdriver.Ie(iedriver)
driver.get("https://www.python.org/")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
#assert "Google" in driver.title
driver.close()
driver.quit()