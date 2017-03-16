#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#create date：2017-3-16
#author：zuosong
import smtplib
import email.MIMEMultipart# import MIMEMultipart
import email.MIMEText# import MIMEText
import email.MIMEBase# import MIMEBase
import mimetypes
import os.path
import time
import sys

sender = "zu.so@163.com"
recipients = "zuosong_0@163.com"
Excel_name = "E:\\Private Doc\\files\\test.xls"#附件名
smtp_server="smtp.163.com"
account="zu.so"
passwd="qeeeeer"

class SendEmail():
    """A class that can send email."""
    def __init__(self,From, To, file_name, server, account, passwd):
        self.sender = From
        self.recipients = To
        self.attachment = file_name
        self.server = server
        self.account = account
        self.passwd = passwd

    def send_email(self):
        # 构造MIMEMultipart对象做为根容器
        main_msg = email.MIMEMultipart.MIMEMultipart()
        text_msg = email.MIMEText.MIMEText("This is a test text to text mime",_charset="utf-8")
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
        main_msg['Subject'] = "attach test "
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
    #mail = SendEmail(sender,recipients,Excel_name,smtp_server,account,passwd)
    #mail.send_email()
    #print "The class SendEmail sent the email!"

#if __name__=="__main__":
#    main()
