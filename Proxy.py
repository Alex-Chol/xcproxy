#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys,os
from HtmlDownload import Htmldownload
from HtmlParse import Htmlparse
from Filework import filework
import math
class proxy(object):
    def __init__(self):
        self.HtmlDownload = Htmldownload()
        self.Htmlparse = Htmlparse()
        self.f = filework()
        
    def progress_bar(self,portion,total):
        # portion，已经完成的数量 ； total 总任务数量
        # return ： 返回true
        part = total / 50
        count = math.ceil(portion / part)
        sys.stdout.write('\r')
        sys.stdout.write(('[%-50s] %.2f%%' % (('>' * count),portion/total*100)))
        sys.stdout.flush()

    def run(self):
        if os.path.exists("ip.txt") == False:
            self.f.write_time()
            ip_pool = []
            response = self.HtmlDownload.get_Highly_anonymous()  # 获取高匿IP页面信息
            if response != None:
                ip_list,port_list,localtion_list,type_list,Effective_time_list,Last_verification_time_list=self.Htmlparse.html_parse(response)
                #a = 3
                #ip_dict = {type_list[a].lower():"http://"+ip_list[a]+":"+port_list[a]}
                #print(ip_dict)
                #is_work = self.HtmlDownload.ip_test(ip_dict)
                #print(is_work)

                total = len(ip_list)
                portion = 0
                print("测试代理服务器中..(每20分钟测试一次)")
                for i in range(0,total):
                    # 最后验证时间最近的有 9 个
                    if i > 9:
                        # 判断是否绝对失效
                        if Effective_time_list[i] == '1分钟':
                            portion += 1
                            self.progress_bar(portion,total)
                            continue # 跳过这个IP，直接验证下一个
                    ip_dict = {type_list[i].lower():"http://"+ip_list[i]+":"+port_list[i]} # 将每个IP与对应端口打包成一个字典
                    # 这里调用IP测试函数，返回一个 boolean ，true就放入ip池
                    is_work = self.HtmlDownload.ip_test(ip_dict)
                    if is_work == True:
                        ip_pool.append(ip_dict)
                    portion += 1
                    self.progress_bar(portion,total)
                print('\n')
                self.f.write_ip_data(ip_pool)
                return ip_pool # 返回ip池  
            else:
                print("获取代理IP失败")
                return None
        elif os.path.exists("ip.txt") == True:
            if self.f.time_judge(): # 若为真，则删除ip.txt文件，重新执行run函数
                os.remove("ip.txt")
                again = proxy()
                again.run()
            ip_pool = self.f.read_ip_list()
            return ip_pool

        

    def show_ip_pool(self):
        response = self.HtmlDownload.get_Highly_anonymous()  # 获取高匿IP页面信息
        ip_list,port_list,localtion_list,type_list,Effective_time_list,Last_verification_time_list=self.Htmlparse.html_parse(response)
        n = 17
        print("-------------------------------------------------------------------------------")
        print("+       IP        + 端口 +       地区      +  类型  +  有效期 +     最后验证  +")
        print("+-----------------+------+-----------------+--------+---------+---------------+")
        for i in range(0,len(ip_list)):
            ip = ip_list[i].ljust(17)
            port = str(port_list[i]).ljust(6)
            length = len(localtion_list[i]) #  5
            localtion = localtion_list[i].ljust(n-length)
            type_ = type_list[i].ljust(8)
            
            Effective_time2 = Effective_time_list[i].split("天")
            if len(Effective_time2)==1:
                Effective_time = Effective_time_list[i].ljust(7)
            else:
                Effective_time = Effective_time_list[i].ljust(8)
            Last_verification_time = Last_verification_time_list[i].ljust(15)
            print("|"+ip+"|"+port+"|"+localtion+"|"+type_+"|"+Effective_time+"|"+Last_verification_time+"|")
            print("+-----------------+------+-----------------+--------+---------+---------------+")


