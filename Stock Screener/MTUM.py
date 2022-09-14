import pandas as pd
import numpy as np

def MTUM3():

    data = pd.read_csv('Dashboard\Stock Screener\SAVE\STOCKS_Daily.csv',index_col = 0,header=[0, 1])
    save = []
    df = pd.DataFrame()
    for  day in range(5,95,5):
      nnn = (data['Close']/data['Close'].shift(day)) * 100

      #Regular
      sss = nnn.tail(day).mean()
      #EMA
      sss2 = nnn.ewm(day).mean()
      save.append(sss2.tail(1))

      df['{}'.format(day)] = sss

    #Regular
    df.to_csv('Dashboard\Stock Screener\SAVE\MTUM_MA.csv')
    print(df)
    #EMA
    df3 = pd.concat(save)
    df3  = df3.set_index([pd.Index([x for x in range(5,95,5)])])
    df3.index.names = ['Ticker']
    df3T = df3.T

    df3T.to_csv('Dashboard\Stock Screener\SAVE\MTUM_EMA.csv')
    print(df3T)

MTUM3()
