# import requests
# from bs4 import BeautifulSoup

# r = requests.get("http://www.zuihaodaxue.com/ARWU2019.html")  # get 请求指定的页面信息
# # print(r.status_code)  # 检查状态码是否正确，状态为 200，说明访问成功
# # print(r.encoding)  # 查看编码方式
# r.encoding = r.apparent_encoding  # 转换成 utf-8 的编码
# html = r.text
# # print(html)
# soup = BeautifulSoup(html, "html.parser")  # 解析世界大学排名
# # print(soup)
# data = soup.find("tbody").children  # 遍历搜索 `tbody` 标签的孩子节点，返回的是一个迭代器
# print(data)
# for tr in data:
#     print(tr)


import requests

try:
    url = "https://www.lanqiao.cn/courses/"
    r = requests.get(url)
    r.raise_for_status  # 查看状态码是否正确
    r.encoding = r.apparent_encoding  # 转换成 utf-8 的编码形式
    demo = r.text  # 获取页面内容并赋值给定义变量 demo
    print(demo)
except:
    print("未能获取页面内容")
