#!/usr/bin/env python
#coding=utf-8

import collections
import os
#with open('str.txt') as file1:
str_raw="China is a great country. I love China. China is my motherland."
str1=str_raw.split(' ')#

print "source string: \n %s"  %str1
print "the number word count:\n %s" %collections.Counter(str1)
print collections.Counter(str1)['was']
