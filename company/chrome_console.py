#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common import action_chains,keys
from time import sleep

Chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome(executable_path=Chrome_path)
browser.get("http://www.baidu.com")


action = action_chains.ActionChains(browser)
#action.key_down(keys.Keys.CONTROL+keys.Keys.SHIFT+'j')
#action.key_up(keys.Keys.CONTROL+keys.Keys.SHIFT+'j')
#action.perform()
action.key_down(keys.Keys.F12)
action.perform()
sleep(5)
browser.quit()
