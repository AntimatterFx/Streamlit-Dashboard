import pandas as pd
import numpy as np

def MACD(df,interval):
    MACD = pd.DataFrame()
    stock_data = df

    s = []
    t = []
    tick = []
    Adj_close = stock_data['Adj Close']
    for i in Adj_close:
        MACD['exp1'] = Adj_close['{}'.format(i)].ewm(span=12, adjust=False).mean()
        MACD['exp2'] = Adj_close['{}'.format(i)].ewm(span=26, adjust=False).mean()

        MACD['macd'] = MACD['exp1'] - MACD['exp2']
        MACD['exp3'] = MACD['macd'].ewm(span=9, adjust=False).mean()

        previous_15 = MACD['exp3'].shift(1)
        previous_45 = MACD['macd'].shift(1)

        Golden = MACD[((MACD['exp3'] <= MACD['macd']) & (previous_15 >= previous_45))]
        Death = MACD[((MACD['exp3'] >= MACD['macd']) & (previous_15 <= previous_45))]

        tick.append(i)

        try:
            s.append(Golden.index[-1])
        except:
            s.append(np.nan)

            #Death
        try:
            t.append(Death.index[-1])
        except:
            t.append(np.nan)

    df2 = pd.DataFrame()
    df2['Ticker'] = tick
    df2['Death MACD'] = t
    df2['Golden MACD'] = s
    df2 = df2.sort_values('Golden MACD',ascending= False)

    if interval == 'Day':
        df2.to_csv('Dashboard\Stock Screener\SAVE\MACD_Daily.csv')
        #display(df2)
    elif interval == 'Weekly':
        df2.to_csv('Dashboard\Stock Screener\SAVE\MACD_Weekly.csv')
        #display(df2)
    else:
        df2.to_csv('Dashboard\Stock Screener\SAVE\MACD_Monthly.csv')
        #display(df2)
df = pd.read_csv('Dashboard\Stock Screener\SAVE\STOCKS_Daily.csv',index_col = 0,header=[0, 1])
df1 = pd.read_csv('Dashboard\Stock Screener\SAVE\STOCKS_Weekly.csv',index_col = 0,header=[0, 1])
#df2 = pd.read_csv(r'Dashboard\Stock Screener\SAVE\STOCKS_Monthly.csv',index_col = 0,header=[0, 1])
MACD(df,'Day')
MACD(df1,'Weekly')

