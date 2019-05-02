# !/usr/bin/python3
# coding:utf-8 
# Author : mahua
# Email : lihh3721@gmail.com
# Time : 2019/4/20 9:15 AM
# FileName : config.py
from configparser import ConfigParser
from API_prac.common import contants


class ReadConfig:

    def __init__(self,encoding="utf-8"):
        #打开配置文件
        self.cf = ConfigParser()
        self.cf.read(contants.global_file,encoding)#加载global文件
        switch = self.cf.getboolean('switch','on')
        if switch:#如果switch打开，则读取预生产环境pre;否则读取test
            self.cf.read(contants.pre_file,encoding)
        else:
            self.cf.read(contants.test_file,encoding)

    def get_strValue(self,section,option):
        return self.cf.get(section,option)

config = ReadConfig()

# if __name__ == '__main__':
#     config = ReadConfig()
