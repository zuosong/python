#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#modified date:2017-2-22
#fixed point:1.在同一个文件内读写操作。读取页面URL地址,将结果写入另一列
#modified date:2017-2-23
#fixed point:1.为兼容不同操作系统，使用xlutils,xlrd,xlwt进行文件读写操作。
#fixed point:1.将状态码为非200的页面URL地址输出到一个txt文档中
#            2.判断页面加载完成与否
#modified date:2017-3-1
#fixed point: 1.修改判断状态码的函数getStatusCode;2.增加一个判断页面是否加载完的函数load_page_done;
#             3.优化写入sheet表中的判断
#发送带附件的邮件使用的module
#modified date:2017-3-13
#fixed point:尝试将对浏览器操作的函数改写成一个class
#modified date:2017-3-14
#fixed point: 1.将读取Excel的三个代码模块放到一个里边去
#             2.将getStatusCode从class中移出去
import smtplib
import email.MIMEMultipart# import MIMEMultipart
import email.MIMEText# import MIMEText
import email.MIMEBase# import MIMEBase
import mimetypes

import os.path
import time
import sys,xdrlib
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import requests #获取页面状态码
import xlrd
#表格的读写操作库 2017-2-23 zs
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
#windows系统下表格文件的读写库
import win32com.client
from win32com.client import Dispatch

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

#set the the path of chromedriver.exe
chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
#数据文件存储名称及路径
file_excel='E:\Private Doc\\files\\file.xls'
error_log = 'E:\Private Doc\\files\\error.txt'
row_start=2#url地址从第2行开始
row_end=57#url地址在第17行结束
send_account = "zu.so@163.com"
receive_account = "zuosong_0@163.com"
#Excel_name = "E:\\Private Doc\\files\\test.xls"#附件名
smtp_server="smtp.163.com"
account="zu.so"
passwd="xxxxxx"

class BrowserOperation():
    """ BrowserOperation class"""
    def __init__(self,url, login_name, passwd , filename):
        self.browser = webdriver.Chrome(executable_path=chrome_path)
        self.browser.set_page_load_timeout(200)#设置页面加载时间200s
        self.url = url
        self.login_name = login_name
        self.passwd = passwd
        self.filename = filename

#Use the webdriver to load the page
#input:url,return:browser object
    def load_page(self):
        try:
            self.browser.get(self.url)
        except TimeoutException:
            self.browser.execute_script('window.stop()')

#Find the login button ,enter the account and password to login The website
#Input:the browser,the user account,password;
    def login_gsb(self):
        self.browser.find_element_by_link_text("登录").click()
        time.sleep(2)
        user = self.browser.find_element_by_xpath("//input[@name='username']")
        user.clear()
        user.send_keys(self.login_name)
        password = self.browser.find_element_by_xpath("//input[@name='password']")
        password.clear()
        password.send_keys(self.passwd)
        time.sleep(1)
        form = self.browser.find_element_by_name("dosubmit")
        form.submit()

#Check the cookie COOKIE_ACCOUNT_LOGIN_TICKET to confirm if login success
#input browser object;return boolean value:if login success return true
    def check_cookies(self):
        rtn_log_cookie = "return document.cookie.includes('COOKIE_ACCOUNT_LOGIN_TICKET');"
        if_log = self.browser.execute_script(rtn_log_cookie)
        return if_log

#close  the browser
    def close_browser(self):
        self.browser.close()

#capture the picture of the page now displaying
#input:browser,the name of pic
    def capture_pic(self):
        self.browser.save_screenshot(self.filename)

#get the performance the page loading
#input:browser,return:load time(ms)
    def get_page_performance(self):
        time1 = self.browser.execute_script("""return window.performance.timing.navigationStart;""")
        time2 = self.browser.execute_script("""return window.performance.timing.loadEventEnd;""")
        return time2 - time1

#判断是否加载页面完成
    def load_page_done(self):
        return self.browser.execute_script("return document.readyState;")=="complete"

#使用requests获取页面状态码
def getStatusCode(url):
     r = requests.get(url, allow_redirects = False)
     return r.status_code

#fixed point:不根据sheet名称查找，根据序号进行查找
def get_url_list(file=file_excel, by_index=0, col_num=6):
    try:
        data = xlrd.open_workbook(file)
        table = data.sheets()[by_index]
        nrows = table.nrows
        ncols = table.ncols
        list = []
        list = table.col_values(col_num)
        return list[row_start:row_end]
    except Exception,e:
        print str(e)

def send_mail2(From,To,file_name,server,account,passwd):
    # 构造MIMEMultipart对象做为根容器
    main_msg = email.MIMEMultipart.MIMEMultipart()

    # 构造MIMEText对象做为邮件显示内容并附加到根容器
    text_msg = email.MIMEText.MIMEText("This is a test text to text mime",_charset="utf-8")
    main_msg.attach(text_msg)
    # 构造MIMEBase对象做为文件附件内容并附加到根容器
    ## 读入文件内容并格式化 [方式1]－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
    data = open(file_name, 'rb')
    ctype,encoding = mimetypes.guess_type(file_name)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype,subtype = ctype.split('/',1)
    file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close()
    email.Encoders.encode_base64(file_msg)#把附件编码
    ## 设置附件头
    basename = os.path.basename(file_name)
    file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头
    main_msg.attach(file_msg)

    # 设置根容器属性
    main_msg['From'] = From
    main_msg['To'] = To
    main_msg['Subject'] = "attach test "
    main_msg['Date'] = email.Utils.formatdate( )

    # 得到格式化后的完整文本
    fullText = main_msg.as_string()

    server = smtplib.SMTP(smtp_server)
    server.login(account,passwd)
    # 用smtp发送邮件
    try:
        server.sendmail(From, To, fullText)
    finally:
        server.quit()

#The main function
def main():
    url_error = []
    fl = open(error_log, 'w')
    rb = open_workbook(file_excel, formatting_info=True )
    for sheet in range(len(rb.sheets())):
        colx = [6, 5, 5]
        printx = [5, 4, 6]
        timex = [2, 2, 7]
        url_list = get_url_list(file_excel,sheet,colx[sheet])
        r_sheet = rb.sheet_by_index(sheet)
        wb = copy(rb)
        w_sheet = wb.get_sheet(sheet)
        for i in range(len(url_list)):
            code = getStatusCode(url_list[i])
            w_sheet.write(2+i, timex[sheet], code)
            if code >= 400:
                url_error.append(url_list[i])
            else:
                browser = BrowserOperation(url_list[i],"18618447716", "addaf", "capture.jpg")
                while (browser.load_page_done() != 1):
                    time.sleep(200)
                browser.load_page()
                loadtime = browser.get_page_performance()
                if (loadtime < 0 or loadtime > 20000 ):
                    w_sheet.write(2+i, printx[sheet], "The page spent too much time loading!")
                else:
                    w_sheet.write(2+i, printx[sheet], loadtime)
                print "The page %s load %d ms."  %(url_list[i],loadtime)
                browser.close_browser()
        wb.save("E:\\Private Doc\\files\\file.xls")
        rb = open_workbook(file_excel, formatting_info=True )

    for i in url_error:
        fl.write(i)
        fl.write('\n')
    fl.close()

if __name__=="__main__":
    main()
