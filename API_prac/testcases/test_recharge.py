# !/usr/bin/python3
# coding:utf-8 
# Author : mahua
# Email : lihh3721@gmail.com
# Time : 2019/4/20 8:50 AM
# FileName : test_recharge.py

import unittest
from API_prac.common.http_request import HttpRequest_session
from API_prac.common import rwExcel
from API_prac.common import contants
from ddt import ddt,data
from API_prac.common import context
from API_prac.common.do_mysql import DoMysql

@ddt
class RechargeTest(unittest.TestCase):
    excel = rwExcel.RWExcel(contants.case_file, 'recharge')
    cases = excel.readExcel()
    @classmethod
    def setUpClass(cls):#setUp:每个执行之前都要实例化一次，改成类方法setUpClass后就只需要在所有的执行之前实例化一次
        cls.http_request = HttpRequest_session()
        cls.mysql = DoMysql()

    @data(*cases)
    def test_recharge(self,case):
        case.data = context.replace(case.data)
        if case.sql:
            sql = eval(case.sql)['sql']
            before = self.mysql.fetch_one(sql)[0]
        resp = self.http_request.http_request(case.method,case.url,case.data)
        actual_code = resp.json()['code']#获取返回的code
        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.writeExcel(case.case_id+1,resp.text,'PASS')
            if case.sql:
                sql = eval(case.sql)['sql']
                after = self.mysql.fetch_one(sql)[0]
                recharge_amount = int(eval(case.data)['amount'])
                print(type(recharge_amount),recharge_amount)
                self.assertEqual(before + recharge_amount,after)
        except AssertionError as e:
            self.excel.writeExcel(case.case_id+1,resp.text,'FAIL')
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()