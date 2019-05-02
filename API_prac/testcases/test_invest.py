# !/usr/bin/python3
# coding:utf-8 
# Author : mahua
# Email : lihh3721@gmail.com
# Time : 2019/4/21 1:43 AM
# FileName : test_invest.py

import unittest
from API_prac.common.http_request import HttpRequest_session
from API_prac.common import rwExcel
from API_prac.common import contants
from ddt import ddt,data
from API_prac.common import context
from API_prac.common import do_mysql

@ddt
class BidLoanTest(unittest.TestCase):
    excel = rwExcel.RWExcel(contants.case_file, 'invest')
    cases = excel.readExcel()
    @classmethod
    def setUpClass(cls):#setUp:每个执行之前都要实例化一次，改成类方法setUpClass后就只需要在所有的执行之前实例化一次
        cls.http_request = HttpRequest_session()
        cls.mysql = do_mysql.DoMysql()

    @data(*cases)
    def test_bigLoan(self,case):
        if case.data.find('noexist_member') > -1:#判断find返回的索引是否=-1，=-1时表示找不到register_phone
            sql = 'SELECT MAX(id) FROM future.member;'
            max_memberId = self.mysql.fetch_one(sql)[0]#查询最大用户id
            noexistMember = int(max_memberId)+1#最大用户id+1
            case.data = case.data.replace('noexist_member',str(noexistMember))#替换参数值,并重新赋值给case.data变量去接收
        if case.data.find('noexist_loan') > -1:#判断find返回的索引是否=-1，=-1时表示找不到noexist_loan
            sql = 'SELECT MAX(id) FROM future.loan;'
            max_loanId = self.mysql.fetch_one(sql)[0]#查询最大标id
            noexistLoan = int(max_loanId)+1#最大手机号码+1
            case.data = case.data.replace('noexist_loan',str(noexistLoan))#替换参数值,并重新赋值给case.data变量去接收
        case.data = context.replace(case.data)
        resp = self.http_request.http_request(case.method,case.url,case.data)
        actual_code = resp.json()['code']#获取返回的code
        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.writeExcel(case.case_id+1,resp.text,'PASS')
            if resp.json()['msg'] == "加标成功" and case.sql:
                sql = eval(case.sql)['sql']
                loan_id = self.mysql.fetch_one(sql)[0]#如果查的是id，则返回的是int
                print(loan_id)
                setattr(context.Context,"loan_id",str(loan_id))
        except AssertionError as e:
            self.excel.writeExcel(case.case_id+1,resp.text,'FAIL')
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()