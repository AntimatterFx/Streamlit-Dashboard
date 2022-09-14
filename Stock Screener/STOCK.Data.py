import yfinance as yf
import datetime as dt
import pandas as pd
import numpy as np

def Daily():
    #df = pd.read_csv('SAVE\Fund.csv')
    #tickers = df['Ticker'].tolist()
    df = pd.read_csv('Dashboard\Stock Screener\SAVE\FUND.csv')
    tickers = df['Tickers'].tolist()
    date_stock = dt.datetime.now() - dt.timedelta(days = 0)
    year_stock = dt.datetime.now() - dt.timedelta(weeks = 104)
    stocks_daily = yf.download(tickers,start = year_stock ,end = date_stock ,threads = True,prepost = True)

    #stocks_daily = stocks_daily[:-1] # removes last row
    stocks_daily.to_csv('Dashboard\Stock Screener\SAVE\STOCKS_Daily.csv')
    stock_data = pd.read_csv('Dashboard\Stock Screener\SAVE\STOCKS_Daily.csv',index_col = 0,header=[0, 1])
    print(stock_data)
def Weekly():
    #df = pd.read_csv('SAVE\Fund.csv')
    #tickers = df['Ticker'].tolist()
    df = pd.read_csv('Dashboard\Stock Screener\SAVE\FUND.csv')
    tickers = df['Tickers'].tolist()
    date_stock = dt.datetime.now() - dt.timedelta(days = 0)
    year_stock = dt.datetime.now() - dt.timedelta(weeks = 380)
    stocks_daily = yf.download(tickers,start = year_stock ,end = date_stock,interval= '1wk',threads = True,prepost = True)

    #stocks_daily = stocks_daily[:-1] # removes last row
    stocks_daily.to_csv('Dashboard\Stock Screener\SAVE\STOCKS_Weekly.csv')
    #stock_data = pd.read_csv('SAVE\STOCKS_Weekly.csv',index_col = 0,header=[0, 1])
    #print(stock_data)
Daily()
Weekly()