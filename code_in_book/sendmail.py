#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '2264215919@qq.com'#�����ʼ�
receivers = ['zuosong@gongsibao.com']  #�����ʼ�

#������������һ���Ǳ����ݣ��ڶ���plain���ñ���ʽ��������urf-8���ñ���
message = MIMEText('Python.', 'plain', 'utf-8')
message['From'] = Header("python", 'utf-8')
message['To'] =  Header("test", 'utf-8')

subject = 'Python SMTP  �����ʼ�'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "���ͳɹ�"
except smtplib.SMTPException:
    print "����ʧ��"
