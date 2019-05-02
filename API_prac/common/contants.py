# !/usr/bin/python3
# coding:utf-8 
# Author : mahua
# Email : lihh3721@gmail.com
# Time : 2019/4/20 1:15 AM
# FileName : contants.py

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取API_prac文件夹的路径
#os.path.abspath(__file__):动态获取当前文件的绝对路径
#os.path.dirname(os.path.abspath(__file__))：获取上一层的文件夹路径

case_file = os.path.join(base_dir,'data','cases02.xlsx')#添加路径

global_file = os.path.join(base_dir,'config','global.conf')

pre_file = os.path.join(base_dir,'config','pre.conf')

test_file = os.path.join(base_dir,'config','test.conf')

log_dir = os.path.join(base_dir,'log')

cases_dir = os.path.join(base_dir,'testcases')

report_dir = os.path.join(base_dir,'reports')
