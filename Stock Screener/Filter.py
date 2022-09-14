import streamlit as st
import pandas as pd 


def Filter(eps,sales):
    pd.set_option('display.max_columns', None)
    df = pd.read_csv('Dashboard\Stock Screener\SAVE\Stocks Table.csv')
    #Fundamentals
    df = df[(df['Sales Q/Q %'] > sales)]  
    df = df[(df['EPS this Y %'] > eps) | (df['EPS next Y %'] > eps)]
    #print(len(df))
    #MACD
    df = df.sort_values('Golden MACD',ascending= False)
        
    

    #Joing MTUM
    df = df[df['MTUM-MA-25'] > 100]
    df = df.sort_values(by = ['Golden MACD','MTUM-MA-25','EPS this Y %'],ascending= False)
  
    #Join Weekly MACD with MA
    df = df.sort_values('Weekly Golden MACD',ascending= False)
    #print(df['Golden MACD'])
    df = df[df['Weekly Golden MACD'] <= df['Golden MACD']]
    #display(df)
    print(len(df))
Filter(15,15)  