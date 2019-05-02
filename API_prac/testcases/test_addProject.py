# !/usr/bin/python3
# coding:utf-8 
# Author : mahua
# Email : lihh3721@gmail.com
# Time : 2019/4/21 12:38 AM
# FileName : test_addProject.py

import unittest
from API_prac.common.http_request import HttpRequest_session
from API_prac.common import rwExcel
from API_prac.common import contants
from ddt import ddt,data
from API_prac.common.config import config
from API_prac.common import context

@ddt
class AddProjectTest(unittest.TestCase):
    excel = rwExcel.RWExcel(contants.case_file, 'add')
    cases = excel.readExcel()
    @classmethod
    def setUpClass(cls):#setUp:每个执行之前都要实例化一次，改成类方法setUpClass后就只需要在所有的执行之前实例化一次
        cls.http_request = HttpRequest_session()

    @data(*cases)
    def test_addProject(self,case):
        #在请求之前替换参数化的值
        case.data = context.replace(case.data)
        resp = self.http_request.http_request(case.method,case.url,case.data)
        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.writeExcel(case.case_id+1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.writeExcel(case.case_id+1,resp.text,'FAIL')
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()