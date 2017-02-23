#date:2017-2-22
#脚本：使用xlrd两种读取Excel文件的方式
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
#����������ȡExcel�����е����ݣ�������file��excel��·����colnameindex:��ͷ���������е�������by_index:��������
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

#�������ƻ�ȡExcel�����е����ݣ�������file:Excel·����colnameindex��ͷ���������е�������by_name:sheet1����
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
