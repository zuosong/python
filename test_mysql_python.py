#!/usr/bin/env python

import MySQLdb

def main():
    print '*** Connecting to database***'
    cxn=MySQLdb.connect(host='localhost', user='root', passwd='hantang@0727', db='test')
    if not cxn:
        print 'ERROR: connection not supported, exiting'
        return

    cur=cxn.cursor()

    print '*** Creating users table***'
    cur.execute('CREATE TABLE users(login VARCHAR(8), uid INT)')
    print '*** Inserting some users***'
    cur.execute("INSERT INTO users VALUES('john', 7000)")
    cur.execute("INSERT INTO users VALUES('jane', 7001)")
    cur.execute("INSERT INTO users VALUES('bob', 7200)")

    print '*** Search for users starting with j***'
    cur.execute("SELECT * FROM users WHERE login LIKE 'j%'")
    for data in cur.fetchall():
        print '%s\t%s' % data

    cur.close()
    cxn.commit()
    cxn.close()

if __name__ == '__main__':
    main()
