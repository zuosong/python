#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '2264215919@qq.com'#发送邮件
receivers = ['zuosong@gongsibao.com']  #接收邮件

#三个参数：第一个是本内容，第二个plain设置本格式，第三个urf-8设置编码
message = MIMEText('Python.', 'plain', 'utf-8')
message['From'] = Header("python", 'utf-8')
message['To'] =  Header("test", 'utf-8')

subject = 'Python SMTP  测试邮件'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "发送成功"
except smtplib.SMTPException:
    print "发送失败"
