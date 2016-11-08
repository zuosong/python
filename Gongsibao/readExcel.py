#!/usr/bin/env python
#-*- coding: utf-8 -*-
import xdrlib,sys
import xlrd
def open_excel(file='file.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
#根据索引获取Excel表格中的数据，参数：file：excel件路径，colnameindex:表头列名所在行的索引，by_index:表的索引
def excel_table_byindex(file = 'file.xlsx',colnameindex=0,by_index=1):
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
                app[colnames[i]] = row[i]
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

def main():
    tables = excel_table_byindex()
    for row in tables:
        print row

    tables = excel_table_byname()
    for row in tables:
        print row

if __name__=="__main__":
    main()
