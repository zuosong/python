#!/bin/bash
for i in `cat links.txt`
do
STATUS_CODE=`curl -o /dev/null -s -w %{http_code} $i`
if [[ $STATUS_CODE -gt 200 ]]; then 
echo "The $i is $STATUS_CODE " >> mail.txt
else
echo -e "$i:\t$STATUS_CODE" >> status.log 
fi
done
blat mail.txt -to 2264215919@qq.com -attach "status.log" -s "系统邮件" -u zuosong@gongsibao.com -pw gongsibao@0727 -charset Gb2312