FILE="status.log"
if [ -f "$FILE" ];then
rm -rf $FILE
else getlinks.sh $1  &&  http_code.sh 
fi
if [ -f "$FILE" ]; then 
blat mail.txt -to 2264215919@qq.com -cc test@gongsibao.com -attach "status.log" -s "系统邮件" -u xxxx@gongsibao.com -pw xxxx@xxx -charset Gb2312
else 
blat mail.txt -to 2264215919@qq.com  -s "系统错误!!" -u test@gongsibao.com -pw fqwwewrw -charset Gb2312
fi 