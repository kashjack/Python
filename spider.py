# !/usr/bin/python
# -*- coding: UTF-8 -*-
# import sys
# import requests
# import urllib.request
# import pandas as pd
# import math
import mysql.connector
# from bs4 import BeautifulSoup

# import urllib.request
# headers = {'User_Agent' : ''}
# response = urllib.request.Request('http://python.org', headers=headers)
# html = urllib.request.urlopen(response)
# result = html.read().decode('utf-8')
# print(result)

# list = [1, 2, 3, 4]
# it = iter(list)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# def hello():
#     print("hello world")
# hello()

# def area(width, height):
#     return width * height

# def print_welcome(name):
#     print("welcome", name)

# print_welcome("Runoob")
# print(area(4, 5))

# a = [66.25, 333, 333, 1, 1234.5]
# print(a.count(333))

# print('命令行参数如下:')
# for i in sys.argv:
#    print(i)

# print('\n\nPython 路径为：', sys.path, '\n')

# str = input("请输入：")
# print("你输入的内容是：", str, str)

# class MyClass:
#     i = 12345
#     def f(self):
#         return self.__class__
# x = MyClass()
# print("MyClass 类的属性i为：", x.i)
# print("MyClass 类的方法f输出为：", x.f())
#
# a = [ 1,2,3,4,5 ]
# print(a[:100])

# params = {'wd': '周杰伦', 'ie': 'utf-8'}
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.30'}
# res = requests.get("https://www.baidu.com/s", params=params, headers=headers)
# print(res.status_code)
# print(res.request.url)

# r = requests.get('https://unsplash.com')
# print(r.text)

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get", params=payload)
# print(r.text)

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """
# soup = BeautifulSoup(html_doc, 'lxml')  #声明BeautifulSoup对象
# find = soup.find('p')  #使用find方法查到第一个p标签
# print("find's return type is ", type(find))  #输出返回值类型
# print("find's content is", find)  #输出find获取的值
# print("find's Tag Name is ", find.name)  #输出标签的名字
# print("find's Attribute(class) is ", find['class'])  #输出标签的class属性值

# markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
# soup = BeautifulSoup(markup)
# comment = soup.b.string
# type(comment)

# 给请求指定一个请求头来模拟chrome浏览器
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
# web_url = 'https://unsplash.com'
# response = requests.get(web_url, headers=headers)  # 向目标url地址发送get请求，返回一个response对象
# result = BeautifulSoup(response.text,'lxml')

# img = result.select('.border-wrap img')[0]
# print('https://github.com{}'.format(img['src']))
# all_a = BeautifulSoup(response.text, 'lxml').find_all('a', class_='cV68d')  # 获取网页中的class为cV68d的所有a标签
# print(all_a)
# for a in all_a:
#     img_str = a['style']  # a标签中完整的style字符串
#     print('a标签的style内容是：', img_str)
#     first_pos = img_str.index('"') + 1
#     second_pos = img_str.index('"',first_pos)
#     img_url = img_str[first_pos: second_pos] #使用Python的切片功能截取双引号之间的内容
#     width_pos = img_url.index('&w=')
#     height_pos = img_url.index('&q=')
#     width_height_str = img_url[width_pos : height_pos]
#     print('高度和宽度数据字符串是：', width_height_str)
#     img_url_final = img_url.replace(width_height_str, '')
#     print('截取后的图片的url是：', img_url_final)


# data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv" #填写url读取
# df = pd.read_csv(data_url)
# df.to_csv('/Users/worldunionyellow/Desktop/test.csv', encoding='utf-8', index=False)

# response = urllib.request.urlopen('https://blog.csdn.net/weixin_43499626')
# print(response.read().decode('utf-8'))


# response = requests.get(url='https://www.cnblogs.com/wyl-0120/p/10358086.html')
# print(response.text)

mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="yourusername",    # 数据库用户名
  passwd="yourpassword"   # 数据库密码
)
 