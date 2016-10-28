# -*- coding:utf-8 -*-
'''
���ʹ�����־
'''
import os
import smtplib
import time
import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_mail(to_list,sub,content): #
    mail_host = "smtp.163.com"
    mail_user = "zu.so"
    mail_pass = "qwerty"
    mail_postfix = "163.com"

    me = "������־" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list
    #�ʼ���
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
            if yes_date in line:
                if "ERROR" in line:
                    finalfile.write(line)

    finally:
        f.close()
        finalfile.close()

def get_yesterday_date():
    today = datetime.datetime.now()
    oneday = today - datetime.timedelta(days=1)
    yes_date = oneday.strftime("%Y-%m-%d")
    return yes_date

if __name__ == '__main__':
    sourcedir = "page.txt"
    objectdir = "error_log.txt"
    mailto_list= "zu.so@163.com"
    yes_date = get_yesterday_date()

    getContent(sourcedir,objectdir)
    if os.path.getsize(objectdir):
        if send_mail(mailto_list,"������־_"+yes_date,objectdir):
            print "���ͳɹ�"
        else:
            print "����ʧ��"
    else:
        print "�޴�����־��δ�����ʼ�"
