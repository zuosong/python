列表页链接地址：
http://www.gongsibao.com/product_1/[1-13].html
详情页链接地址：

源地址：http://www.gongsibao.com/product_249/detail/[id].html
重定向到
目标地址：
http://deve_item.gongsibao.com/item/[id].html

#!/bin/bash
id=1
while [ $id -le 13 ]
do
        all.sh  http://www.gongsibao.com/product_1/$id.html 
        id=$(( $id + 1 ))
done 