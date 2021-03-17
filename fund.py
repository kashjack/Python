'''
Author: your name
Date: 2021-01-26 14:14:12
LastEditTime: 2021-01-26 14:28:24
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /PythonProject/fund.py
'''


import requests
from bs4 import BeautifulSoup
import bs4
import json

response = requests.get("http://fundgz.1234567.com.cn/js/001186.js?rt=1463558676006")
j = json.loads(response.text)
print(j["name"])
print(response.text)