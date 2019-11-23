#!/usr/bin/env python
#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
class Htmlparse(object):
    def html_parse(self,response):
        try:
            #这里是BeautifulSoup的网页分析代码
            r = BeautifulSoup(response,'html5lib')
            div = r.find_all('div',class_='clearfix proxies')[0]
            tbody = div.find('tbody')
            tr = tbody.find_all('tr')
            ip_list = []
            port_list = []
            localtion_list = []
            type_list = []
            Effective_time_list = []
            Last_verification_time_list = []
            for each in range(1,len(tr)):
                ip = tr[each].find_all('td')[1].text  # IP
                port = tr[each].find_all('td')[2].text  # 端口
                localtion = tr[each].find_all('td')[3].text.strip()  # 地区
                type_ = tr[each].find_all('td')[5].text.strip() #   协议类型
                Effective_time = tr[each].find_all('td')[8].text.strip() # 有效时间
                Last_verification_time = tr[each].find_all('td')[9].text.strip() # 最后验证时间
                ip_list.append(ip)
                port_list.append(port)
                localtion_list.append(localtion)
                type_list.append(type_)
                Effective_time_list.append(Effective_time)
                Last_verification_time_list.append(Last_verification_time)
            return ip_list,port_list,localtion_list,type_list,Effective_time_list,Last_verification_time_list
        except Exception as e:
            print(e)
            exit()