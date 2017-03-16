#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#create date：2017-3-16
#author：zuosong
#modified date:2017-3-16
#fixed point:1.发送邮件的主题和正文文本可通过参数传递，并且支持中文。
import smtplib
import email.MIMEMultipart# import MIMEMultipart
import email.MIMEText# import MIMEText
import email.MIMEBase# import MIMEBase
import mimetypes
import os.path
import time
import sys

#sender = "zu.so@163.com"
#recipients = "zuosong_0@163.com"
#Excel_name = "E:\\Private Doc\\files\\test.xls"#附件名
#smtp_server="smtp.163.com"
#account="zu.so"
#passwd="qwertyu"

class SendEmail():
    """A class that can send email."""
    def __init__(self,From, To, subject, body_msg, file_name, server, account, passwd):
        self.sender = From
        self.recipients = To
        self.subject = subject
        self.body_msg = body_msg
        self.attachment = file_name
        self.server = server
        self.account = account
        self.passwd = passwd

    def send_email(self):
        # 构造MIMEMultipart对象做为根容器
        main_msg = email.MIMEMultipart.MIMEMultipart()
        text_msg = email.MIMEText.MIMEText(self.body_msg, _charset="utf-8")
        main_msg.attach(text_msg)
        # 构造MIMEBase对象做为文件附件内容并附加到根容器
        ## 读入文件内容并格式化 [方式1]－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
        data = open(self.attachment, 'rb')
        ctype,encoding = mimetypes.guess_type(self.attachment)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype,subtype = ctype.split('/',1)
        file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read())
        data.close()
        email.Encoders.encode_base64(file_msg)#把附件编码
        ## 设置附件头
        basename = os.path.basename(self.attachment)
        file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头
        main_msg.attach(file_msg)
        # 设置根容器属性
        main_msg['From'] = self.sender
        main_msg['To'] = self.recipients
        main_msg['Subject'] = self.subject
        main_msg['Date'] = email.Utils.formatdate()
        # 得到格式化后的完整文本
        fullText = main_msg.as_string()

        server = smtplib.SMTP(self.server)
        server.login(self.account,self.passwd)
        # 用smtp发送邮件
        try:
            server.sendmail(self.sender, self.recipients, fullText)
        finally:
            server.quit()

#def main():
#   mail = SendEmail(sender,recipients,"主题", "正文", Excel_name,smtp_server,account,passwd)
#  mail.send_email()
#    print "邮件已经发送成功！"

#if __name__=="__main__":
#    main()
