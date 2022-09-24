import pandas as pd
def MA(): 
    MA20 = []
    MA50 = []
    MA100 = []
    MA150 = []
    MA200 = []
    Price = []
    tick = []
    low = []
    high = []

    stock_data = pd.read_csv('Dashboard\Stock_Screener\SAVE\STOCKS_Daily.csv',index_col = 0,header=[0, 1])
    df3 = stock_data['Adj Close']
    df1 = pd.DataFrame()
    for i in df3.columns:
        df1['20MA'] = df3['{}'.format(i)].rolling(20).mean()
        df1['50MA'] = df3['{}'.format(i)].rolling(50).mean()
        df1['100MA'] = df3['{}'.format(i)].rolling(100).mean()
        df1['150MA'] = df3['{}'.format(i)].rolling(150).mean()
        df1['200MA'] = df3['{}'.format(i)].rolling(200).mean()

        low52 = min(stock_data['Low']['{}'.format(i)][-260:])
        high52 = max(stock_data['High']['{}'.format(i)][-260:])

        try:
            Price.append(df3['{}'.format(i)][-1])

            low.append(low52)
            high.append(high52)

            MA20.append(df1['20MA'][-1])
            MA50.append(df1['50MA'][-1])
            MA100.append(df1['100MA'][-1])
            MA150.append(df1['150MA'][-1])
            MA200.append(df1['200MA'][-1])
            tick.append(i)
        except:
            0
    df2 = pd.DataFrame()
    df2['Ticker'] = tick
    df2['Price'] = Price
    df2['52-Week-Low'] = low
    df2['52-Week-High'] = high
    df2['20-MA'] = MA20
    df2['50-MA'] = MA50
    df2['100-MA'] = MA100
    df2['150-MA'] = MA150
    df2['200-MA'] = MA200
    df2 = df2.set_index('Ticker')
    df2.to_csv('Dashboard\Stock_Screener\SAVE\MA.csv')
    print(df2)

def EMA():
    EMA20 = []
    EMA50 = []
    EMA100 = []
    EMA150 = []
    EMA200 = []
    tick = []

    stock_data = pd.read_csv('Dashboard\Stock_Screener\SAVE\STOCKS_Daily.csv',index_col = 0,header=[0, 1])
    df3 = stock_data['Adj Close']
    df1 = pd.DataFrame()
    for i in df3.columns:

        df1['20EMA'] =  df3['{}'.format(i)].ewm(20).mean()
        df1['50EMA'] =  df3['{}'.format(i)].ewm(50).mean()
        df1['150EMA'] =  df3['{}'.format(i)].ewm(150).mean()
        df1['100EMA'] =  df3['{}'.format(i)].ewm(100).mean()
        df1['200EMA'] = df3['{}'.format(i)].ewm(200).mean()

        try:
            EMA20.append(df1['20EMA'][-1])
            EMA150.append(df1['150EMA'][-1])
            EMA50.append(df1['50EMA'][-1])
            EMA100.append(df1['100EMA'][-1])
            EMA200.append(df1['200EMA'][-1])
            tick.append(i)
        except:
            0
    df2 = pd.DataFrame()
    df2['Ticker'] = tick
    df2['20-EMA'] = EMA20
    df2['50-EMA'] = EMA50
    df2['100-EMA'] = EMA100
    df2['150-EMA'] = EMA150
    df2['200-EMA'] = EMA200
    df2 = df2.set_index('Ticker')
    df2.to_csv('Dashboard\Stock_Screener\SAVE\EMA.csv')

MA()
EMA()


