# !/usr/bin/python3
# coding:utf-8 
# Author : mahua
# Email : lihh3721@gmail.com
# Time : 2019/3/24 9:32 PM
# FileName : http_request.py

import requests
from API_prac.common.config import config
from API_prac.common import logger

logger = logger.get_logger(__name__)

class HttpRequest:

    def http_request(self,method,url,data=None,json=None,cookies=None):
        '''完成http的get请求或post请求
        :method 请求方法 可以是get or post
        :url 请求地址
        :param 请求参数，字典的格式'''
        method = method.upper()
        if type(data) == str:#防止从excel读取数据时返回字符串
            data = eval(data)#将字符串转换为字典

        #拼接请求的url
        url = config.get_strValue('env','test')+url
        logger.debug('请求url：{}'.format(url))
        logger.debug('请求data：{}'.format(data))

        if method=='GET': # 发送一个get请求:如果请求有参数的话 就要以字典的形式传递过去
                resp=requests.get(url,params=data,cookies=cookies)#响应结果消息实体  包含：响应头 响应报文 状态码
                # print('get响应报文:',resp.text)#响应报文
        elif method=='POST':#除了get就是post 所以这里设定else情况是发送一个post请求
            if json:
                resp = requests.post(url,json=json,cookies=cookies)
            else:
                resp = requests.post(url,data=data,cookies=cookies)
        else:
            resp = None
            logger.error('No support method')
        return resp

class HttpRequest_session:
    #创建一个session
    def __init__(self):
        self.session = requests.sessions.session()

    def http_request(self,method,url,data=None,json=None):
        '''完成http的get请求或post请求
        :method 请求方法 可以是get or post
        :url 请求地址
        :param 请求参数，字典的格式'''
        method = method.upper()
        if type(data) == str:#防止从excel读取数据时返回字符串
            data = eval(data)

        #拼接请求的url
        url = config.get_strValue('env','test')+url
        logger.debug('请求url：{}'.format(url))
        logger.debug('请求data：{}'.format(data))


        if method=='GET': # 发送一个get请求:如果请求有参数的话 就要以字典的形式传递过去
                resp=self.session.request(method=method,url=url,params=data)#响应结果消息实体  包含：响应头 响应报文 状态码
                # print('get响应报文:',resp.text)#响应报文
        elif method=='POST':#除了get就是post 所以这里设定else情况是发送一个post请求
            if json:
                resp=self.session.request(method=method,url=url,json=data)
            else:
                resp=self.session.request(method=method,url=url,data=data)
        else:
            resp = None
            logger.error('No support method')
        return resp
    #关闭session
    def close(self):
        self.session.close()


#测试代码 3-2号的课程  复习:记忆力差
if __name__ == '__main__':
    pass
    # http_request1 = HttpRequest()
    # params = {"mobilephone": "15810447878", "pwd": "123456"}
    # resp_1 = http_request1.http_request('pOST', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data=params)
    # print(resp_1.status_code)
    # print(resp_1.text)
    # print(resp_1.cookies)
    # params = {"mobilephone": "15810447878", "amount": "1000"}
    # resp_2 = http_request1.http_request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=params,cookies=resp_1.cookies)
    # print(resp_2.status_code)
    # print(resp_2.text)
    # print(resp_2.cookies)
    #
    #
    # http_request2 = HttpRequest_session()
    # params = {"mobilephone": "15810447878", "pwd": "123456"}
    # resp = http_request2.http_request('pOST', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data=params)
    # params = {"mobilephone": "15810447878", "amount": "1000"}
    # resp2 = http_request2.http_request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=params)
    # http_request2.close()
    # print(resp2.status_code)
    # print(resp2.text)
    # print(resp2.cookies)