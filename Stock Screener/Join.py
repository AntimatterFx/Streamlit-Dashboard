import pandas as pd 
import yfinance as yf
import numpy as np  
import datetime as dt

exec(open('Dashboard\Stock Screener\ETFS.py').read())
print('1')
exec(open('Dashboard\Stock Screener\FIN-FUND.py').read())
print('2')
exec(open('Dashboard\Stock Screener\STOCK.Data.py').read())
print('3')
exec(open('Dashboard\Stock Screener\EMA+MA.py').read())
print('4')
exec(open('Dashboard\Stock Screener\MTUM.py').read())
print('5')
exec(open('Dashboard\Stock Screener\MACD.py').read())
print('6')

def Join():
    global n, mm
    #Join the Data based on MA
    df2 = pd.read_csv('Dashboard\Stock Screener\SAVE\MA.csv',index_col= 0)
    ult = df2.copy()

    #Join the Data based on Fundmental 
    df = pd.read_csv('Dashboard\Stock Screener\SAVE\Fund.csv',index_col = 0)
    ult = ult[ult.index.isin(df.index)]

    ult['Sector'] = df['Sector'] 
    ult['Industry'] = df['Industry']
    
    ult['P/E'] = df['P/E']
    ult['PEG'] = df['PEG']
    ult['P/FCF'] = df['P/FCF']
  
    ult['Sales Q/Q %'] = df['Sales Q/Q %']
    ult['EPS this Y %'] = df['EPS this Y %']
    try:
        ult['EPS next Y %'] = df['EPS next Y']
    except:
        ult['EPS next Y %'] = df['EPS next Y %']
    #print(len(ult))
    
    #Join MACD with MA
    df = pd.read_csv('Dashboard\Stock Screener\SAVE\MACD_Daily.csv',index_col= 0)
    df = df.set_index('Ticker')    
    df = df[df.index.isin(ult.index)]

    ult[ult.index.isin(df.index)]
    ultdf = ult.join(df)  
    ultdf = ultdf.sort_values('Golden MACD',ascending= False)
    #print(len(ultdf))   
     
    #Joing Volume #Fix Later
    """Vol = pd.read_csv('SAVE\Volume.csv',index_col= 0)
    mm = Vol
    ultdf = ultdf[ultdf.index.isin(Vol.index)]
    print(len(ultdf)) """ 
    
    #Joing MTUM
    EMA = pd.read_csv('Dashboard\Stock Screener\SAVE\MTUM_EMA.csv',index_col= 0)
    MA = pd.read_csv('Dashboard\Stock Screener\SAVE\MTUM_MA.csv',index_col= 0)
    #print(len(MA))
    #print(len(EMA))
    MA = MA[MA.index.isin(ultdf.index)]
    EMA = EMA[EMA.index.isin(ultdf.index)]
    
    ultdf['MTUM-MA-25'] = MA['25']
    ultdf['MTUM-EMA-25'] = EMA['25']
    ultdf = ultdf.sort_values(by = ['Golden MACD','MTUM-MA-25','EPS this Y %'],ascending= False)
    #print(len(ultdf))   
    
    #Join Weekly MACD with MA
    weeklydf = pd.read_csv('Dashboard\Stock Screener\SAVE\MACD_Weekly.csv',index_col= 0)
    weeklydf = weeklydf.rename(columns = {'Death MACD':'Weekly Death MACD','Golden MACD':'Weekly Golden MACD'})
    weeklydf = weeklydf.set_index('Ticker')
    weeklydf = weeklydf[weeklydf.index.isin(ultdf.index)]

    ultdf[ultdf.index.isin(weeklydf.index)]
    ultdf = ultdf.join(weeklydf, how='outer')  
    ultdf = ultdf.sort_values('Weekly Golden MACD',ascending= False)
    #\display(ultdf)
    
    ultdf.to_csv('Dashboard\Stock Screener\SAVE\Stocks Table.csv')
    #print(len(ultdf))   
    
    #date_now = dt.datetime.now().strftime("%m-%d-%y")
    #path = r'Stocks_Rec.xlsx'
    #with pd.ExcelWriter(path, engine='openpyxl', mode='a') as writer:  
        #ultdf.to_excel(writer, sheet_name=f'{date_now}')
        #print(ultdf
Join()