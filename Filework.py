#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time,datetime
import json
class filework(object):
    def write_time(self):#写入当前系统时间
        f = open("ip.txt","w+") # 以w+模式打开文件，文件数据会被清空
        f.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        f.write(' ')
        f.close()

    def write_ip_data(self,ip_list):# 将测试完毕的代理池写入文件
        f = open("ip.txt","a+")
        data = json.dumps(ip_list) #将列表解析为字符串，写入文件
        f.write(data)
        f.write('\n')
        f.close()

    def read_ip_list(self):# 读取文件中的代理池，返回一个列表
        f = open("ip.txt","r")
        f.seek(20,0) # 将指针右移20个字符，0代表从文件头部开始
        data = f.read()
        f.close()
        result = json.loads(data) # 将字符串解析为列表
        return result

    def time_judge(self):
        now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        time1 = datetime.datetime.fromtimestamp(time.mktime(time.strptime(now,'%Y-%m-%d %H:%M:%S')))
        f = open('ip.txt','r')
        old_time = f.read(19)
        f.close()
        time2 = datetime.datetime.fromtimestamp(time.mktime(time.strptime(old_time,'%Y-%m-%d %H:%M:%S')))
        delta = time1 - time2
        boo = delta > datetime.timedelta(minutes=20)
        return boo