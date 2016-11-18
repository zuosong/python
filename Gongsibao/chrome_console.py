from selenium import webdriver
from selenium.webdriver.common import action_chains,keys

Chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome(executable_path=Chrome_path)
browser.get("http://www.baidu.com")


action = action_chains.ActionChains(browser)
#action.send_keys(keys.Keys.CONTROL+keys.Keys.SHIFT+'j')
#action.perform()
action.send_keys(keys.Keys.F12)
action.perform()
