#!/usr/bin/env python
#-*- coding: utf-8 -*-
import requests
#from bs4 import BeautifulSoup
import Error_info
class Htmldownload(object):
    def get_Highly_anonymous(self): # 获取高匿IP页面响应
        try:
            header = {
                'Host':'www.xicidaili.com',
                'Referer':'https://www.xicidaili.com/',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
            }
            link = r'https://www.xicidaili.com/nn'
            response = requests.get(link,headers=header)
            if response.status_code != 200:
                raise Error_info.Download_error(response.status_code)
            else:
                return response.text
        except Error_info.Download_error as e:
            print(e)
            return None
        except Exception as e:
            print(e)
            return None
        

    def ip_test(self,proxy): # 传入一个IP
        header = { 
            'Host':'200019.ip138.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
        }
        link = "http://200019.ip138.com/"
        try:
            response = requests.get(link,headers=header,proxies=proxy,timeout=5)
            if response.status_code != 200:
                raise Error_info.Download_error(response.status_code)
            else: 
                '''soup = BeautifulSoup(response.text,"html5lib")
                result = soup.find('p').text
                print(result)'''
                return True
        except Error_info.Download_error as e:
            print("IP测试"+e)
            exit()
        except requests.exceptions.Timeout:
            return False
        except requests.exceptions.ProxyError:
            return False
        except Exception as e:
            print("发生未知异常")
            return False
        
            