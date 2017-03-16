#!/usr/bin/python
# -*- coding: utf-8 -*-
"""单元测试代码
"""
import unittest
#路径增加company的文件路径
import sys
sys.path.append("E:\\Private Doc\\code\\company")
from GSB_test import rwExcel

class RwExcelTestCase(unittest.TestCase):
    def setUp(self):
        self.excel = rwExcel(r'E:\Private Doc\\files\\file.xlsx')
        self.excel.setCell(1,1,1,5)
        #self.excel.getCell(1,1,1)
    def test_getCell(self):
        num = self.excel.getCell(1,1,1)
        self.assertEqual(num ,5 )

    def tearDown(self):
        self.excel.save()
        self.excel.close()


def suite():
    suite =unittest.TestSuite()
    suite.addTest(RwExcelTestCase("testgetCell"))
    return suite

if __name__ =='__main__':
    unittest.main(defaultTest = 'suite')
