#!/usr/bin/env python
#-*- coding: utf-8 -*-
import xdrlib,sys
import xlrd
import time
import urllib2
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def open_excel(file='file.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
#根据索引获取Excel表格中的数据，参数：file：excel件路径，colnameindex:表头列名所在行的索引，by_index:表的索引
def excel_table_byindex(file = 'file.xlsx',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    ncols = table.ncols
    colnames = table.row_values(colnameindex)
    list = []
    for rownum in range(0,nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[1]] = row[1]
            list.append(app)
    return list


#根据名称获取Excel表格中的数据，参数：file:Excel路径，colnameindex表头列名所在行的索引，by_name:sheet1名称
def excel_table_byname(file='file.xlsx',colnameindex=0,by_name=u'Sheet2'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows
    colnames = table.row_values(colnameindex)
    list = []
    for rownum in range(0,nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list

#获取指定一列的值
def excel_table_col_I(file = 'file.xlsx',by_index=1,col_num=1):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    ncols = table.ncols
    list = []
    list = table.col_values(col_num)
    return list

def open_url(url):
    Chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=Chrome_path) # Get local
    browser.get(url)
    time.sleep(1)
    browser.close()

def get_status_code(url):
    try:
        response = urllib2.urlopen(url,timeout=5)
    except urllib2.URLError as e:
        if hasattr(e, 'code'):
            print 'The url',url,'retrun Error code:',e.code
        elif hasattr(e, 'reason'):
            print 'Reason:',e.reason
    finally:
        if response:
            #print 'The url',url,'Code: ',response.getcode()
            response.close()



def main():
    #tables = excel_table_byindex()
    #for row in tables:
    #    print row

    #tables = excel_table_byname()
    #for row in tables:
    #    print row
    tables = excel_table_col_I('file.xlsx',1,6)
    #print tables[2]
    for i in range(len(tables)):
        print tables[i]
        open_url(tables[i])
        get_status_code(tables[i])

if __name__=="__main__":
    main()
