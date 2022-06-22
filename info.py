'''
Author: kashjack
Date: 2021-09-16 16:10:35
LastEditTime: 2021-10-08 16:22:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /Quant/info.py
'''

import jqdatasdk
import os
import pandas
import time
import random


def auth1():
    jqdatasdk.auth('18637675552', '675552')


def auth2():
    jqdatasdk.auth('17328785156', '785156')


def code(code):
    '''获取标准化code'''
    return jqdatasdk.normalize_code(code)


def getSourcePath(path):
    '''获取本地资源路径
    '''
    return os.getcwd() + '/code/source/' + path


def get_csv(path):
    '''从本地获取csv文件'''
    df = pandas.read_csv(getSourcePath(path))
    return df


def getAllStocks():
    auth1()
    '''从jk获取csv文件'''
    # 所有股票代码
    stocks = jqdatasdk.get_all_securities(['stock'])
    de = pandas.DataFrame(stocks)
    de.to_csv(getSourcePath('stocks.csv'))
    return


def limit():
    # 今日剩余额度
    get_query_count = jqdatasdk.get_query_count()
    print('limit', get_query_count)


def randomDate():
    # 随机时间
    start = 1420041600  # 生成开始时间戳 2015-01-01
    end = int(time.time())  # 生成结束时间戳
    # # 随机生成1个日期字符串
    t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    date = time.strftime("%Y-%m-%d", date_touple)
    return date
