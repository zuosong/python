#date:2017-2-22
# -*- coding: utf-8 -*-
#发送邮件脚本

import smtplib
import email.MIMEMultipart# import MIMEMultipart
import email.MIMEText# import MIMEText
import email.MIMEBase# import MIMEBase
import os.path
import mimetypes
send_account = "zu.so@163.com"
receive_account = "zuosong_0@163.com"
Excel_name = "E:\\Private Doc\\files\\test.xls"#附件名
smtp_server="smtp.163.com"
account="zu.so"
passwd="#####"
from SendEmail import SendEmail

def send_mail2(From,To,file_name,server,account,passwd):

    # 构造MIMEMultipart对象做为根容器
    main_msg = email.MIMEMultipart.MIMEMultipart()

    # 构造MIMEText对象做为邮件显示内容并附加到根容器
    text_msg = email.MIMEText.MIMEText("This is a test text to test mime",_charset="utf-8")
    main_msg.attach(text_msg)

    ## 读入文件内容并格式化 [方式1]－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
    data = open(file_name, 'rb')
    ctype,encoding = mimetypes.guess_type(file_name)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype,subtype = ctype.split('/',1)
    file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close( )
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
    server.login(account,passwd) #仅smtp服务器需要验证时
    # 用smtp发送邮件
    try:
        server.sendmail(From, To, fullText)
    finally:
        server.quit()

def main():
    #send_mail2(send_account,receive_account,Excel_name,smtp_server,account,passwd)
    mail = SendEmail(send_account,receive_account,Excel_name,smtp_server,account,passwd)
    mail.send_email()

if __name__=="__main__":
    main()
