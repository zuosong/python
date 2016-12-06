curl $1 -o links.html
sed 's/\"/\n/g' links.html | grep '^http://www.gongsibao.com' > links.txt
rm links.html 