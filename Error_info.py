#!/usr/bin/env python
#-*- coding: utf-8 -*-
#本模块的基类
class Main_error(Exception):
    def __init__(self,e):
        self.e = e
    def __str__(self):
        return "发生未知异常:"+self.e

# 页面响应异常
class Download_error(Main_error):
    def __init__(self,status_code):
        # 定义用户输入的数据
        self.status_code = status_code
    def __str__(self):
        # 返回异常信息
        return "网页响应异常,状态码:"+str(self.status_code)

class request_error(Main_error):
    def __init__(self,e):
        self.e = e
    def __str__(self):
        return self.e

