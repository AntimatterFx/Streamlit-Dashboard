import pandas as pd
import numpy as np
import requests
import re
import datetime as dt

def ETFs():
    """ Gets Etf holding from ZACKs"""
    Tickers = ['QQQ','QQQJ','TAN','PTF','PSJ','XSW','MTUM','ARKK','ARKQ','ARKF','ARKG','ARKW','ARKX','FFTY','HACK','IZRL','TFMC'] # Can adjust these ,'MTUM'
    #Tickers = ['QQQ','QQQJ','TAN','PTF','PSJ','XSW','MTUM','ARKK'] # Can adjust these ,'MTUM'


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
    }

    ETF = []

    url = "https://www.zacks.com/funds/etf/{}/holding"
    with requests.Session() as req:
        req.headers.update(headers)
        for tick in Tickers: #
            r = req.get(url.format(tick),verify=True)#SO I can scrap data 
            #print(f"Extracting: {r.url}")
            goal = re.findall(r'etf\\\/(.*?)\\', r.text)
            #print(len(goal))
            ETF.append(goal)
            #print(tickers)

    df = pd.DataFrame(ETF, Tickers) # converts ETF to df
    df = df.T #Tranposes the DataFrame to make Tickers the column name

    stocks = []
    for i in df.columns:
        df1 = pd.DataFrame()
        df1['Ticker'] = df['{}'.format(i)].dropna()
        df1['ETF'] = i
        stocks.append(df1)
    allstocks = pd.concat(stocks)
    allstocks_etf = allstocks.groupby(['Ticker'])['ETF'].apply(','.join).reset_index() #reset index is a must or wont be a df
    allstocks_etf.to_csv('Dashboard\Stock Screener\SAVE\ETFs.csv')
    print('Done')
ETFs()

#allstocks_etf.to_csv('Dashboard\Stock Screener\SAVE\ETFs.csv')