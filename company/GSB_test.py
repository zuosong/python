#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
import smtplib
import email.MIMEMultipart# import MIMEMultipart
import email.MIMEText# import MIMEText
import email.MIMEBase# import MIMEBase
import os.path
import mimetypes
import time
import sys,xdrlib
import urllib2
import xlrd
import win32com.client
import smtplib
import email.MIMEMultipart# import MIMEMultipart
import email.MIMEText# import MIMEText
import email.MIMEBase# import MIMEBase
import os.path
import mimetypes
from win32com.client import Dispatch
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
#set the the path of chromedriver.exe
chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
#数据文件存储名称及路径
file_excel='E:\Private Doc\\files\\file.xlsx'
row_start=2#url地址从第2行开始
row_end=27#url地址在第17行结束
send_account = "zu.so@163.com"
receive_account = "zuosong_0@163.com"
Excel_name = "E:\\Private Doc\\files\\test.xls"#附件名
smtp_server="smtp.163.com"
account="zu.so"
passwd="qwertyui"

class rwExcel:
      """A utility to make it easier to get at Excel.    Remembering
      to save the data is your problem, as is    error handling.
      Operates on one workbook at a time."""
      def __init__(self, filename=None):  #打开文件或者新建文件（如果不存在的话）
          self.xlApp = win32com.client.Dispatch('Excel.Application')
          if filename:
              self.filename = filename
              self.xlBook = self.xlApp.Workbooks.Open(filename)
          else:
              self.xlBook = self.xlApp.Workbooks.Add()
              self.filename = ''

      def save(self, newfilename=None):  #保存文件
          if newfilename:
              self.filename = newfilename
              self.xlBook.SaveAs(newfilename)
          else:
              self.xlBook.Save()
      def close(self):  #关闭文件
          self.xlBook.Close(SaveChanges=0)
          del self.xlApp
      def getCell(self, sheet, row, col):  #获取单元格的数据
          "Get value of one cell"
          sht = self.xlBook.Worksheets(sheet)
          return sht.Cells(row, col).Value
      def setCell(self, sheet, row, col, value):  #设置单元格的数据
          "set value of one cell"
          sht = self.xlBook.Worksheets(sheet)
          sht.Cells(row, col).Value = value

#Use the webdriver to load the page
#input:url,return:browser object
def load_page(url):
    browser = webdriver.Chrome(executable_path=chrome_path) # Get local session of Chrome
    loadpage=url
    browser.get(loadpage) # Load page
    return browser

#Find the login button ,enter the account and password to login The website
#Input:the browser,the user account,password;
def login_gsb(obj,account,passwd):
    browser=obj
    browser.find_element_by_link_text("登录").click()
    time.sleep(2)
    user = browser.find_element_by_xpath("//input[@name='username']")
    user.clear()
    user.send_keys(account)
    password = browser.find_element_by_xpath("//input[@name='password']")
    password.clear()
    password.send_keys(passwd)
    time.sleep(1)
    form = browser.find_element_by_name("dosubmit")
    form.submit()

#Check the cookie COOKIE_ACCOUNT_LOGIN_TICKET to confirm if login success
#input browser object;return boolean value:if login success return true
def check_cookies(obj):
    browser= obj
    rtn_log_cookie="return document.cookie.includes('COOKIE_ACCOUNT_LOGIN_TICKET');"
    if_log = browser.execute_script(rtn_log_cookie)
    return if_log

#close  the browser
def close_browser(obj):
    browser = obj
    browser.close()

#capture the picture of the page now displaying
#input:browser,the name of pic
def capture_pic(obj,save_fn="capture.png"):
    browser=obj
    save_pic=save_fn
    browser.save_screenshot(save_pic)

#get the performance the page loading
#input:browser,return:load time(ms)
def get_page_performance(obj):
    browser=obj
    time1=browser.execute_script("""return window.performance.timing.navigationStart;""")
    time2=browser.execute_script("""return window.performance.timing.loadEventEnd;""")
    return time2-time1

def get_url_list(file=file_excel,by_name=u'Sheet1',col_num=6):
    try:
        data = xlrd.open_workbook(file)
        table = data.sheet_by_name(by_name)
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
    dict_performance={}
    dict_httpcode={}
    url_list = get_url_list(file_excel,u'Sheet1',6)
    xls = rwExcel(r'E:\\Private Doc\\files\\test.xls')
    for i in range(len(url_list)):
        response = None
        xls.setCell('sheet1',2+i,'A',url_list[i])
        try:
            response = urllib2.urlopen(url_list[i],timeout=5)
        except urllib2.URLError as e:
            if hasattr(e, 'code'):
                #print 'Error code:',e.code
                #dict_httpcode[url_list[i]]=e.code
                xls.setCell('sheet1',2+i,'B',e.code)
            elif hasattr(e, 'reason'):
                #print 'Reason:',e.reason
                #dict_httpcode[url_list[i]]=e.reason
                xls.setCell('sheet1',2+i,'B',e.reason)
        finally:
            if response:
                #dict_httpcode[url_list[i]]=response.getcode()
                xls.setCell('sheet1',2+i,'B',response.getcode())
                browser=load_page(url_list[i])
                #if check_cookies(browser):
                    #login_gsb(browser,"qwrr","qqqqqqqq")
                #account=raw_input("Please enter your phone number: ")
                #passwd=raw_input("Please enter your password: ")
                #
                loadtime=get_page_performance(browser)
                xls.setCell('sheet1',2+i,'C',loadtime)
                #print "The loadtime of the page is: %d ms " %loadtime
                #dict_performance[url_list[i]]=loadtime
                time.sleep(1)
                close_browser(browser)
                response.close()
    xls.save()
    xls.close()
    send_mail2(send_account,receive_account,Excel_name,smtp_server,account,passwd)

if __name__=="__main__":
    main()
