#!user/bin/env python

import string
import keyword
alphas = string.letters + '_'
nums = string.digits
kwlist = keyword.kwlist
print 'Welcome to the Identifier Checker v1.0'

myInput = raw_input('Identifier to test?')

if myInput[0] not in alphas:
    print '''invalid:first symbol must be alphabetic'''
else:
    for otherChar in myInput[1:]:
    
        if otherChar not in alphas+nums:
            print '''invalid:remaining symbols must be alphanumeric'''
            break
    else:
        print "okay as an identifier"
        if myInput in kwlist:
            print "but it is a kewword!"