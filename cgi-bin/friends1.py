#!/usr/bin/env python

import cgi

reshtml = ''' Content-Type:text/heml \n
<HTML>
<HEAD>
<TITLE>
Friends CGI Deom(dynamic screen)
</TITLE>
</HEAD>
<BODY>
<H3>Friends list for:<I>%s</I></H3>
Your name is:<B>%s</B><P>
You have <B>%s</B> friends
</BODY>
</HTML>'''
form = cgi.FieldStorage()
who = form['person'].value
howmany = form ['howmany'].value
print reshtml %(who,who,howmany)
