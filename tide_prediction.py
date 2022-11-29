# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 17:12:37 2021

@author: Neraliel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import utide


def utime(dtindex):
    # transform from pandas.DatetimeIndex to utide time
    return dates.date2num(dtindex.to_pydatetime())


df_Cher = pd.read_csv('13_2017.txt', comment='#', delimiter=';', usecols=[0, 1], names=["date", "sl"],
                      parse_dates={'datetime': [0]})
df_Cher.set_index('datetime', inplace=True)

t = utime(df_Cher.index)
seal = np.array(df_Cher.sl)
coef = utide.solve(t, seal, lat=49.633731, epoch='1770-01-01')
t_rec = pd.date_range('17/12/1850', '18/12/1850', freq='1MIN')
predict = utide.reconstruct(utime(t_rec), coef, epoch='1770-01-01')
df_pred = pd.DataFrame(data=predict['h'], index=t_rec, columns=['predicted'])
