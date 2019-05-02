# !/usr/bin/python3
# coding:utf-8 
# Author : mahua
# Email : lihh3721@gmail.com
# Time : 2019/4/20 1:45 AM
# FileName : test_login.py

import unittest
from API_prac.common.http_request import HttpRequest_session
from API_prac.common import rwExcel
from API_prac.common import contants
from ddt import ddt,data
from API_prac.common import context
from API_prac.common import logger

logger = logger.get_logger(__name__)

@ddt
class LoginTest(unittest.TestCase):
    excel = rwExcel.RWExcel(contants.case_file, 'login')
    cases = excel.readExcel()
    @classmethod
    def setUpClass(cls):#setUp:每个执行之前都要实例化一次，改成类方法setUpClass后就只需要在所有的执行之前实例化一次
        logger.info('准备测试前置')
        cls.http_request = HttpRequest_session()

    @data(*cases)
    def test_login(self,case):
        logger.info('开始测试：{}'.format(case.title))
        case.data = context.replace(case.data)
        resp = self.http_request.http_request(case.method,case.url,case.data)
        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.writeExcel(case.case_id+1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.writeExcel(case.case_id+1,resp.text,'FAIL')
            logger.error('测试报错了，{}'.format(e))
            raise e
        logger.info('结束测试：{}'.format(case.title))
    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()