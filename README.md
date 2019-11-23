# xcproxy
食用方法：
将该项目所有文件放在一个文件夹中，重命名为xcproxy
在一个py文件中添加代码 --> import xcproxy
即可导入该模块

接口方法有两个，分别为：

# 1、建立IP池，导出TXT文件到当前文件夹。
xcproxy.get_proxy()


# 2、输出当前所有IP，无论可用还是不可用
a = xcproxy.show_proxy()
print(a)
