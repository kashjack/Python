# !/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

df1 = pd.DataFrame({'A': np.random.randn(10), 'B': np.random.randn(10)})
df2 = pd.DataFrame({'C': np.random.randn(10), 'D': np.random.randn(10)})

# 写入数据文件
# df.to_csv('test.csv', encoding='utf-8', index=False)
# df.to_excel('test.xlsx', encoding='utf-8', index=False)

df1.to_hdf('test.h5', key='df1')
df2.to_hdf('test.h5', key='df2', format='table')

print("*****示例文件写入成功*****")
