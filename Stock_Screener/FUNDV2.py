import requests
import time
import pandas as pd
import numpy as np

def Convert(dfs,stock):
    names = []
    names_values = []
    try:
        df = dfs[5]
        basic_df = dfs[4]
        for i in range(0,len(df.columns)):
            if i%2 == 0:
                #display(df[i])
                names.append(df[i])
            else:
                names_values.append(df[i])
                
        Index_names = pd.concat(names).reset_index(drop= True)
        Index_Values = pd.concat(names_values).reset_index(drop= True)
        df1 = pd.DataFrame()
        df1[f'{stock}'] = Index_names
        df1['Values'] = Index_Values
        #df2 = df1['Values'].replace('%','')
        df2 = df1['Values'].replace('-','0')
        #df1 = df1.fillna('-1')
        
        #Adding stock basic info
        basic_df = basic_df.T.drop(0,axis = 1)
        basic_df = basic_df.rename({1:'Company',2:'Sector'},axis=1)
        basic_df.index = [stock]

        #Adds Percentages to name
        not_add_percentage = df1[~df1['Values'].str.contains('%')]
        not_add_percentage  = not_add_percentage[f'{stock}']
        add_percentage = df1[df1['Values'].str.contains('%')]
        add_percentage  = add_percentage[f'{stock}'] + ' %'

        #Converts that column so I can remove %
        df1['Values'] = df1['Values'].convert_dtypes(str)
        df1['Values'] = df1['Values'].str.replace('%','')

        df1['Values'] = df1['Values'].str.replace('K','e3')
        df1['Values'] = df1['Values'].str.replace('M','e6')
        df1['Values'] = df1['Values'].str.replace('B','e9')

        df1['Index'] = pd.concat([not_add_percentage,add_percentage]).sort_index()
        df1.index = df1['Index']
        df1 = df1.drop([f'{stock}','Index'], axis=1)

        df1.columns = [f'{stock}']
        df2  = df1.T
        #print(df2)
        Names_of_Tickers.append(stock)
        #display(df2)
        for i in df2.columns: #converts everything to float
            try:
                df2['{}'.format(i)] = df2['{}'.format(i)].astype(float)
            except:
                #print(i)
                0
        df3 =  basic_df.join(df2, how='outer')
        #display(df2.T,basic_df,df3)
        return df3
    except:
        print(f'2-{stock}')
        


def getFinData():
  global Names_of_Tickers 
  Names_of_Tickers = []
  saved = []
  stocks = pd.read_csv('Dashboard\Stock_Screener\SAVE\ETFs.csv')
  print(len(stocks))
  stocks = stocks.drop_duplicates('Ticker')
  print(len(stocks))
  #stocks = pd.read_csv('SAVE\ETFs.csv')
  start = time.time()
  for stock in stocks['Ticker']:
    try:
      url = f'https://finviz.com/quote.ashx?t={stock}'
    
      header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
      }

      r = requests.get(url, headers=header)

      dfs = pd.read_html(r.text)
      d = Convert(dfs,stock)
      
      saved.append(d)
    except:
      print('1')
  #print(saved) 
  savethisdf = pd.concat(saved,ignore_index=True)
  print(len(savethisdf),len(Names_of_Tickers ))
  savethisdf['Tickers'] = Names_of_Tickers
  
  savethisdf = savethisdf.set_index('Tickers',inplace=False)
  #savethisdf.index.names = ['Tickers']
  savethisdf[['Sector','Industry','Country']] = savethisdf['Sector'].str.split('|',expand=True)
  savethisdf = savethisdf[savethisdf.columns[0:74]]
  savethisdf = savethisdf.replace('-',np.nan)
  savethisdf.to_csv('Dashboard\Stock_Screener\SAVE\FUND.csv')
  end = time.time()
  print(end - start)
  #return saved
getFinData()