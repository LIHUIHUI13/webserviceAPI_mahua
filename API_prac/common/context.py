# !/usr/bin/python3
# coding:utf-8 
# Author : mahua
# Email : lihh3721@gmail.com
# Time : 2019/4/21 10:40 PM
# FileName : context.py
import re
from API_prac.common.config import config
import configparser

class Context:
    loan_id = None
def replace(data):
    p = "#(.*?)#"
    while re.search(p,data):
        m = re.search(p,data)  # 从任意位置开始找，找第一个就返回Match object，如果没有找到则返回None
        g = m.group(1)  # 拿到参数化的key
        try:
            v = config.get_strValue('user',g)  # 根据key取配置文件的值
        except configparser.NoOptionError as e:
            if hasattr(Context,g):
                v = getattr(Context, g)  # 根据key取Context类里面g（参数化的key）的值
            else:
                print('找不到该参数的值')
                raise e
        #记得替换后的内容，继续用data接收
        data = re.sub(p,v,data,count=1)  # 查找并替换,count:查找替换的次数
    return(data)



