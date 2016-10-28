#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#Filename:checklinks.py
#version 0.1
'''
The code check the links of gongsibao hantang to confirm they can visit
'''

import sys
import urllib2
import os
import smtplib
import time
import datetime
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def status_code():
    f = open("page.txt","r")
    file = open("out.txt","w+")
    savedStdout = sys.stdout #save the standard output
    sys.stdout = file #the standard output changed to file out.txt

    urlList = f.readlines()
    response = None
    for url in urlList:
        #print url
        try:
          response = urllib2.urlopen(url,timeout=5)
        except urllib2.URLError as e:
          if hasattr(e, 'code'):
            print 'The url',url,'retrun Error code:',e.code
          elif hasattr(e, 'reason'):
            print 'Reason:',e.reason
        finally:
          if response:
            #print 'The url',url,'Code: ',response.getcode()
            response.close()
    
    sys.stdout = savedStdout #change the output to the screen
    
def send_mail(to_list,sub,content): #
    mail_host = "smtp.163.com"
    mail_user = "zu.so"
    mail_pass = "zs@mail2"
    mail_postfix = "163.com"

    me = "公司宝" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list
    #
    part = MIMEText(open(objectdir,'r').read(),_charset='gb2312')
    msg.attach(part)

    #part = MIMEApplication(open(objectdir,'rb').read())
    #part.add_header('Content-Disposition','attachment',filename = "error_log.txt")
    #msg.attach(part)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False

def getContent(resouce,final):
    f = open(resouce,'rb')
    finalfile = open(final,'wb')
    try:
        for line in f:
            finalfile.write(line)

    finally:
        f.close()
        finalfile.close()


if __name__ == '__main__':
    status_code()
    sourcedir = "out.txt"
    objectdir = "error_log.txt"
    mailto_list= "zu.so@163.com"
    time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

    getContent(sourcedir,objectdir)
    if os.path.getsize(objectdir):
        if send_mail(mailto_list," "+time,objectdir):
            print "邮件发送成功!"
        else:
            print "邮件发送失败!"
    else:
        print  "No errorlog,the mail was not sended"
