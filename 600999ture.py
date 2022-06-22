'''
Author: kashjack
Date: 2021-09-15 15:31:54
LastEditTime: 2021-09-30 18:27:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /Quant/Unit1.py
'''
# from jqdatasdk import *
import jqdatasdk as jk
import pandas as pd
import info


def set_csv():
    info.auth1()
    '''从jk获取csv文件'''
    df = jk.get_price(
        info.code('600999'), start_date='2021-09-28 00:00:00', end_date='2021-09-30 00:00:00')
    de = pd.DataFrame(df)
    de.to_csv(info.getSourcePath('600999.csv'))
    return


do_time = 0
do_date = ''
account = 0
holding_num = 0
holding_value = 0


def printLog(sell_point, buy_point, price):
    global do_time, account, holding_num, holding_value, do_date
    showAll = True
    if do_date == 'today' or showAll:
        print(do_time, do_date, 'holding_num:', holding_num, 'account:',
              account, 'earnings', round(holding_value + account, 2))
    if do_time == 2:
        print(sell_point, buy_point, price)
        print('\n')


def do(buy_rate, sell_rate):
    '''doSomething'''
    global do_time, account, holding_num, holding_value, do_date
    buy_point = 0
    sell_point = 0
    step = 5 * int(do_time / 10 + 1)
    buy_num = step
    sell_num = step
    do_index = 0
    buy_time = 0
    for index, row in info.get_csv('600999ture.csv').iterrows():
        if index == 0:
            do_index = 0
            do_time = do_time + 1
            price = row['high']
            holding_num = buy_num
            account = round(account - buy_num * price * 100.03, 2)
            buy_point = round(price * (100 - buy_rate + 12) / 100, 2)
            sell_point = round(price * (100 + sell_rate) / 100, 2)
            do_date = row['date']
            holding_value = round(holding_num * row['close'] * 100, 2)
            printLog(sell_point, buy_point, price)
        # 如果high高于卖点，就出
        if (row['high'] > sell_point):
            do_index = index
            do_time = do_time + 1
            price = sell_point
            buy_point = round(price * (100 - buy_rate) / 100, 2)
            sell_point = round(price * (100 + sell_rate) / 100, 2)
            # 连续卖出
            if (buy_time < 0):
                sell_num = sell_num + step
            else:
                sell_num = step
            if (holding_num <= sell_num):
                holding_value = round(holding_num * row['close'] * 100, 2)
                continue
            buy_time = -1
            buy_num = step
            holding_num = holding_num - sell_num
            account = round(account + sell_num * price * 99.87, 2)
            do_date = row['date']
            holding_value = round(holding_num * row['close'] * 100, 2)
            printLog(sell_point, buy_point, price)
        # 如果low低于买点，就入
        if (row['low'] < buy_point):
            do_time = do_time + 1
            price = buy_point
            buy_point = round(price * (100 - buy_rate) / 100, 2)
            sell_point = round(price * (100 + sell_rate) / 100, 2)
            # 连续买入
            if (buy_time > 0):
                buy_num = buy_num + step
            else:
                buy_num = step
            buy_time = 1
            sell_num = step
            holding_num = holding_num + buy_num
            account = round(account - buy_num * price * 100.03, 2)
            do_date = row['date']
            holding_value = round(holding_num * row['close'] * 100, 2)
            printLog(sell_point, buy_point, price)
        holding_value = round(holding_num * row['close'] * 100, 2)
    # do_date = 'today'
    # printLog(sell_point, buy_point, price)


# set_csv()
do(14, 14)


# for index, row in df.iterrows():
#     print(index, row['Name'])
