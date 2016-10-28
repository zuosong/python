#!/usr/bin/env python

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.163.com'
POP3SVR= 'pop3.163.com'
popacnt='zu.so'
mailpswd='qwerty'


origHdrs = ['From:zu.so@163.com','To:zuosong_0@163.com','Subject:test msg']
origBody = ['xxx','yyy','zzz']
origMsg= '\r\n\r\n'.join(['\r\n'.join(origHdrs),'\r\n'.join(origBody)])

sendSvr=SMTP(SMTPSVR)
sendSvr.login(popacnt,mailpswd)
errs = sendSvr.sendmail('zu.so@163.com',('zuosong_0@163.com','2264215919@qq.com'),origMsg)
sendSvr.quit()
assert len(errs) ==0,errs
sleep(10)

recvSvr = POP3(POP3SVR)
recvSvr.user('zuosong_0')
recvSvr.pass_('qwerty')
rsp,msg,siz = recvSvr.retr(recvSvr.stat()[0])

sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody
