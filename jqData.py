'''
Author: kashjack
Date: 2021-09-30 16:25:31
LastEditTime: 2021-10-08 16:30:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /Quant/code/jqData.py
'''
import jqdatasdk
import info
import pandas


def set_csv(num, end_dt):
    info.auth1()
    stocks = pandas.read_csv(info.getSourcePath('stocks.csv'))
    stockName = []
    yesterday = []
    today = []
    yesterday_date = ''
    today_date = ''
    isRed = []
    for stock in stocks.values:
        info_list = jqdatasdk.get_bars(stock[0], num, '1d', fields=[
            'date', 'volume', 'open', 'close'], end_dt=end_dt)
        stockName.append(stock[1])
        yesterday_value = 0
        today_value = 0
        isRed_value = False
        print(info_list)
        return
        for index, row in info_list.iterrows():
            if index == 0:
                yesterday_value = row['volume']
            if index == 1:
                today_value = row['volume']
            isRed_value = (row['close'] - row['open'] < 0)
        yesterday.append(yesterday_value)
        today.append(today_value)
        isRed.append(isRed_value)
        if yesterday_date == '':
            yesterday_date = info_list.values[0][0]
            today_date = info_list.values[1][0]
        # print(info_list)
    dict = {'stockName': stockName,
            yesterday_date: yesterday, today_date: today, 'isRed': isRed}
    de = pandas.DataFrame(dict)
    de.to_csv(info.getSourcePath('daysVolume.csv'))


def get_stock_list():
    for index, row in info.get_csv('towDayVolume.csv').iterrows():
        first = row['2021-09-30']
        second = row['2021-10-08']
        isRed = row['isRed']
        if first > 0 and second > 0 and isRed and (first * 2 < second):
            print(row['stockName'])


def get_stock_list4(num, end_dt):
    """
        获取若干天内正市盈率最近一天交易量是前面所有交易量最大值的两倍且是最近3天是红柱
        num：若干天数
        end_dt：指定结束日期
    """
    if num < 3:
        return
    # 所有股票代码
    stocks = positive_pe_ratio(end_dt)
    my_stocks = []
    for stock in stocks:
        # 获取对应股票代码的交易量
        info_list = get_bars(stock, num, '1d', fields=[
            'volume', 'open', 'close'], end_dt=end_dt)
        volume_list = info_list['volume']
        close_list = info_list['close']
        open_list = info_list['open']
        # 有些数据是空的，加个判断防止报错
        if (volume_list.size > num - 1) & (close_list.size > num - 1) & (open_list.size > num - 1):
            volume_last = volume_list[num - 1]
            volume_list[num - 1] = 0
            volume_max = max(volume_list)
            close_price = close_list[num - 1]
            open_price = open_list[num - 1]
            close_price2 = close_list[num - 2]
            open_price2 = open_list[num - 2]
            close_price3 = close_list[num - 3]
            open_price3 = open_list[num - 3]
            # 有些数据是0，防止作为除数报错
            if (volume_last > 0) & (volume_max > 0):
                # 策略是最近一天交易量 / 前num天交易量最大值  > 2且最近3天是红柱
                if ((volume_last / volume_max) > 2) & (close_price > open_price) & (close_price2 > open_price2) & (
                        close_price3 > open_price3):
                    my_stocks.append(stock)
    print(my_stocks)
    print('over')


def positive_pe_ratio(end_dt):
    # 正市盈率
    q = query(valuation).filter(valuation.pe_ratio > 0)
    fund_data = list(get_fundamentals(q, date=end_dt)['code'])
    return fund_data


def get_stock_list6(end_dt):
    """
        交易量第二天是第一天的两倍，第三天是第一天的三倍，三根红柱
    """
    # 所有股票代码
    stocks = list(get_all_securities(['stock']).index)
    my_stocks = []
    for stock in stocks:
        # 获取对应股票代码的交易量
        info_list = get_bars(stock, 3, '1d', fields=['volume', 'open', 'close'], end_dt=end_dt)
        volume_list = info_list['volume']
        close_list = info_list['close']
        open_list = info_list['open']
        # 有些数据是空的，加个判断防止报错
        if (volume_list.size > 2) & (close_list.size > 2) & (open_list.size > 2):
            close_price0 = close_list[0]
            open_price0 = open_list[0]
            volume0 = volume_list[0]
            close_price1 = close_list[1]
            open_price1 = open_list[1]
            volume1 = volume_list[1]
            close_price2 = close_list[2]
            open_price2 = open_list[2]
            volume2 = volume_list[2]

            # 有些数据是0，防止作为除数报错
            if (volume2 > 0) & (volume1 > 0) & (volume0 > 0):
                # 策略是交易量第二天是第一天的两倍，第三天是第一天的三倍且最近3天是红柱
                if (volume1 / volume0 > 2) & (volume2 / volume0 > 3) & (close_price2 > open_price2) & (
                        close_price1 > open_price1) & (close_price0 > open_price0):
                    my_stocks.append(stock)
    print(my_stocks)
    print('over')


set_csv()
# get_stock_list()
# get_stock_list2(7, '2021-10-08')
