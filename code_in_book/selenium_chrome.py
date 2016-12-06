#coding = utf-8
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get('http://www.gongsibao.com')
print driver.title
driver.quit()
