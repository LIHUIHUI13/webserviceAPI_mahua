# !/usr/bin/python3
# coding:utf-8 
# Author : mahua
# Email : lihh3721@gmail.com
# Time : 2019/5/3 12:14 AM
# FileName : logger.py

import logging
from API_prac.common import contants
from API_prac.common.config import config

def get_logger(name):

    logger = logging.getLogger(name=name)
    logger.setLevel('DEBUG') #定义日志收集级别

    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s : %(lineno)d]'
    formatter = logging.Formatter(fmt)

    console_handler = logging.StreamHandler()#指定输出渠道为控制台
    console_handler.setLevel(config.get_strValue('LOG','console_level'))#定义日志输出级别
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(contants.log_dir + '/case.log')
    file_handler.setLevel(config.get_strValue('LOG','file_level'))
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)#将控制台的输出渠道添加到logger对象
    logger.addHandler(file_handler)
    return logger

if __name__ == '__main__':

    logger = get_logger('mahua')
    logger.debug('这是一个调试')
    logger.info('测试开始啦')
    logger.warning('这是一个warning警告')
    logger.error('这是一个错误error')
    logger.critical('这是一个致命问题')
