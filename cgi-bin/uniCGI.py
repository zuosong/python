# -*- coding: utf-8 -*-
#!/usr/bin/env python

CODEC = 'UTF-8'
UNICODE_HELLO=u'''
Hello!
\u00A1Hola!
\u4F60\u597D!
'''

print 'Content-Type: text/html;charset=%s\r' %CODEC
print '\r'
print '<HTML><HEAD><TITLE>Unicode CGI Demo </TITLE></HEAD>'
print '<BODY>'
print UNICODE_HELLO.encode(CODEC)
print '</BODY></HTML>'
