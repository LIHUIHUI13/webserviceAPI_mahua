# !/usr/bin/python3
# coding:utf-8 
# Author : mahua
# Email : lihh3721@gmail.com
# Time : 2019/5/3 2:07 AM
# FileName : run.py

# import sys
# sys.path.append('./') #project根目录地址

import unittest
import HTMLTestRunnerNew
from API_prac.common import contants
"""
当用例过多时，不采用以下方法。选择defaultTestLoader下的discover方法加载

# # 创建测试套件：测试用例的容器
# suite = unittest.TestSuite()
# from API_prac.testcases import test_invest,test_login,test_addProject,test_recharge,test_register
# # 第一种: 通过模块加载
# loader = unittest.TestLoader() #测试用例加载器
# suite.addTest(loader.loadTestsFromModule(test_register))
# suite.addTest(loader.loadTestsFromModule(test_addProject))
# suite.addTest(loader.loadTestsFromModule(test_recharge))
# suite.addTest(loader.loadTestsFromModule(test_login))
# suite.addTest(loader.loadTestsFromModule(test_invest))
"""


discover = unittest.defaultTestLoader.discover(contants.cases_dir,'test_*.py')

# 执行并生成测试报告
with open(contants.report_dir + '/report.html','wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title='麻花-自动化测试报告',
        description='mahua',
        tester='mahua'
    )
    runner.run(discover)