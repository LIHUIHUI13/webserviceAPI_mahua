# -*- coding:utf-8 -*-
# Author: mahua
# Email: lihh3721@gmail.com
# Date: 2019/4/26 19:45
# FileName: log_output.py

import logging
from API_prac.common.config import config

class mylog:
    def __init__(self,logName,logFileName):
        self.logName = logName
        self.logFileName = logFileName

    def logOutput(self):
        my_logger = logging.getLogger(self.logName)
        my_logger.setLevel(config.get_strValue('LOG','level_1')) #设定收集的级别

        ch = logging.StreamHandler() #指定输出到控制台
        ch.setLevel(config.get_strValue('LOG','level_2')) #指定输出信息级别
        ch.setFormatter('%(asctime)s-%(filename)s-%(levelname)s-日志信息: %(message)s') #指定控制台输出格式

        file_handler = logging.FileHandler(self.logFileName, encoding='utf-8') #指定输出文本渠道 handler
        file_handler.setLevel(config.get_strValue('LOG','level_2'))  # 设定输出信息的级别
        file_handler.setFormatter('%(asctime)s-%(filename)s-%(levelname)s-日志信息: %(message)s') #指定文件输出格式

        #将输出渠道添加到handler
        my_logger.addHandler(ch)
        my_logger.addHandler(file_handler)
        #打印log信息
        my_logger.debug(config.get_strValue('LOG','debugMsg'))
        my_logger.info(config.get_strValue('LOG','infoMsg'))
        my_logger.warning(config.get_strValue('LOG','warningMsg'))
        my_logger.error(config.get_strValue('LOG','errorMsg'))
        my_logger.critical(config.get_strValue('LOG','criticalMsg'))

if __name__ == '__main__':
    pass