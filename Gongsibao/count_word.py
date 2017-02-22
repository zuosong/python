#!/usr/bin/env python
#coding=utf-8
#date:2017-2-22
#分割一句话为一个个单词，然后统计每个单词的出现次数
import collections
import os
#with open('str.txt') as file1:
str_raw="China is a great country. I love China. China is my motherland."
str1=str_raw.split(' ')#

print "source string: \n %s"  %str1
print "the number word count:\n %s" %collections.Counter(str1)
print collections.Counter(str1)['was']
