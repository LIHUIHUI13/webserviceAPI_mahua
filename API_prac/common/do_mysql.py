# !/usr/bin/python3
# coding:utf-8 
# Author : mahua
# Email : lihh3721@gmail.com
# Time : 2019/4/21 1:39 PM
# FileName : do_mysql.py
import pymysql
from API_prac.common.config import config

class DoMysql:

    def __init__(self):
        host = config.get_strValue('db','host')
        user = config.get_strValue('db','user')
        password = config.get_strValue('db','password')
        port = config.get_strValue('db','port')
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=int(port))#创建连接
        # self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)  # 新建一个游标对象
        self.cursor = self.mysql.cursor()  # 新建一个游标对象


    def fetch_one(self,sql):#获取查询结果集里面最近的一条数据返回
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()

    def fetch_all(self,sql):#获取全部结果集
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()#关闭查询
        self.mysql.close()#关闭连接

if __name__ == '__main__':
    mysql = DoMysql()
    sql = "SELECT * from future.member where mobilephone='15283312747';"
    result = mysql.fetch_one(sql)[0]
    print(type(result),result)
    print(result)
    mysql.close()