'''
Author: your name
Date: 2021-01-22 17:29:47
LastEditTime: 2021-01-22 17:56:08
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /PythonProject/beautifulSoup.py
'''
import  requests
from bs4 import BeautifulSoup
import bs4

r = requests.get("https://labfile.oss.aliyuncs.com/courses/2184/2019%E8%BD%AF%E7%A7%91%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E5%AD%A6%E6%9C%AF%E6%8E%92%E5%90%8D.html")
r.encoding = r.apparent_encoding  # 转换成 utf-8 的编码
html = r.text  # 获取页面内容
soup = BeautifulSoup(html, "html.parser")# 解析世界大学排名的页面
data = soup.find("tbody").children
info = []  # 定义一个列表去保存最后需要的数据
for tr in data:
  if isinstance(tr, bs4.element.Tag):  # 判断 tr 是否是 bs4 标签类型的元素
    tds = tr.find_all('td')  # 把 tr 标签中的所有 td 标签的内容存储在列表 tds
    info.append([tds[0].string, tds[1].string, tds[4].string])# 把排名、大学名字、总分放入 info 列表
print(info)

