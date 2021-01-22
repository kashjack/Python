# !/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy
import pandas

df1 = pandas.DataFrame({'A': numpy.random.randn(10), 'B': numpy.random.randn(10)})
df2 = pandas.DataFrame({'C': numpy.random.randn(10), 'D': numpy.random.randn(10)})

# 写入数据文件
df1.to_csv('test.csv', encoding='utf-8', index=False)
df2.to_excel('test.xlsx', encoding='utf-8', index=False)


print("*****示例文件写入成功*****")
