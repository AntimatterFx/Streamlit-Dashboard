import finviz
import datetime as dt
import pandas as pd
import numpy as np

def FundamentalV2():
    """ Makes a dataframe  from finviz dict and removes unwanted things """
    df = pd.read_csv('Dashboard\Stock Screener\SAVE\ETFs.csv',index_col = 0)
    Tickers = df['Ticker'].tolist()
    stock_data = []
    tick = []

    for i in Tickers:

        try:
            fin = finviz.get_stock(i)
            tick.append(i)
            df = pd.DataFrame.from_dict(fin,orient ='index')
            stock_data.append(df.T)
        except:
            0
    maindf = pd.concat(stock_data).reset_index(drop = True)
    trash  = ['Index','Shortable','Employees','Prev Close','Change','Payout','Recom', 'SMA20', 'SMA50', 'SMA200','Optionable','Country','Shs Outstand','Shs Float','Income','Sales','52W Range']
    maindf = maindf.drop(columns= trash)
    maindf['Ticker'] = tick
    return CLEAN_1(maindf)

def CLEAN_1(maindf):
    """ Adds '%' to column name with rows with % and removes them"""
    l  = maindf.columns
    old_names = []
    new_names = []
    for i in l:
        #print(i)
        try:
            s  = maindf['{}'.format(i)].str.contains('%')
            if any(s) == True:
                maindf[i] = maindf[i].str.strip('%')
                maindf[i] = maindf[i].str.strip(',')
                old_names.append('{}'.format(i))
                new_names.append('{} %'.format(i))
            else:
                0
        except:
            0
    dictonary = dict(zip(old_names,new_names))
    maindf = maindf.rename(columns = dictonary)

    return Clean_Float(maindf)

def Clean_Float(maindf):
    """ Converts columns into float so you they are usable"""
    maindf = maindf
    maindf = maindf.replace('-',0)
    maindf['Market Cap 2'] =  maindf['Market Cap']
    change = ['Market Cap']

    for i in change: #changes letter to str number
        maindf[i] = maindf[i].str.replace('B','e9')
        maindf[i] = maindf[i].str.replace('M','e6')
        maindf[i] = maindf[i].str.replace('K','e3')


    for i in maindf.columns: #converts everything to float
        try:
            maindf['{}'.format(i)] = maindf['{}'.format(i)].astype(float)
        except:
            0

    return Clean_Date(maindf)


def Clean_Date(df):
    Change = ['Earnings']
    maindf = df
    for i in Change:
        maindf[i] = maindf[i].str.replace('AMC','')
        maindf[i] = maindf[i].str.replace('BMO','')
        maindf[i] = maindf[i].str.replace('BMO','')
        maindf[i] = maindf[i].str.replace(' ','')

        maindf[i] = maindf[i].str.replace('Jan','01/')
        maindf[i] = maindf[i].str.replace('Feb','02/')
        maindf[i] = maindf[i].str.replace('Mar','03/')
        maindf[i] = maindf[i].str.replace('Apr','04/')
        maindf[i] = maindf[i].str.replace('May','05/')
        maindf[i] = maindf[i].str.replace('Jun','06/')
        maindf[i] = maindf[i].str.replace('Jul','07/')
        maindf[i] = maindf[i].str.replace('Aug','08/')
        maindf[i] = maindf[i].str.replace('Sep','09/')
        maindf[i] = maindf[i].str.replace('Oct','10/')
        maindf[i] = maindf[i].str.replace('Nov','11/')
        maindf[i] = maindf[i].str.replace('Dec','12/')
    now = dt.datetime.now()
    date_time = now.strftime("%m/%d")

    maindf['Earnings'] = np.where(maindf['Earnings'] < date_time ,'NAN',maindf['Earnings'])
    #display(maindf.sort_values(['Market Cap'],ascending = False))
    print(maindf['Ticker'])
    maindf =  maindf.set_index('Ticker')
    #display(maindf)
    maindf.to_csv('Dashboard\Stock Screener\SAVE\Fund.csv')
    print('Done')

FundamentalV2()