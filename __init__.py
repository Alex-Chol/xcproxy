#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
from os import path
curPath = path.abspath(path.dirname(__file__))
sys.path.append(curPath)
from Proxy import proxy


# 在测试IP服务器之前就要过滤好IP  √
# 在测试完成后创建一个IP池文件，20分钟过期 √
# 添加一个错误类，用来返回错误信息  √
# 添加一个显示IP池的功能 √
# 可以让用户自由选择爬取页面前几个IP，节省时间（默认爬取整个页面IP）
# 用回调函数 代替 直接调用  测试函数 

start = proxy()  # 定义主类

def get_proxy():
    result = start.run() # 调用主类的函数
    return result
    
def show_proxy():
    start.show_ip_pool()

get_proxy()
