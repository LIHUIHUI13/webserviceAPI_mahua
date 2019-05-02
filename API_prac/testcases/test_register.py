# !/usr/bin/python3
# coding:utf-8 
# Author : mahua
# Email : lihh3721@gmail.com
# Time : 2019/4/21 1:51 PM
# FileName : test_register.py

import unittest
from API_prac.common.http_request import HttpRequest_session
from API_prac.common import rwExcel
from API_prac.common import contants
from ddt import ddt,data
from API_prac.common import do_mysql
from API_prac.common import context

@ddt
class RegisterTest(unittest.TestCase):
    excel = rwExcel.RWExcel(contants.case_file, 'register')
    cases = excel.readExcel()
    @classmethod
    def setUpClass(cls):#setUp:每个执行之前都要实例化一次，改成类方法setUpClass后就只需要在所有的执行之前实例化一次
        cls.http_request = HttpRequest_session()
        cls.mysql = do_mysql.DoMysql()

    @data(*cases)
    def test_register(self,case):
        if case.data.find('register_phone') > -1:#判断find返回的索引是否=-1，=-1时表示找不到register_phone
            sql = "SELECT MAX(mobilephone) from future.member where mobilephone like '1528331%';"
            max_phone = self.mysql.fetch_one(sql)[0]#查询前缀是1825076的最大手机号码
            max_phone = int(max_phone)+1#最大手机号码+1
            case.data = case.data.replace('register_phone',str(max_phone))#替换参数值,并重新赋值给case.data变量去接收
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
        cls.mysql.close()