#Dashboard\Main\Scripts\activate
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import os
today = dt.datetime.now().strftime("%Y-%m-%d")
path = f'Dashboard\Saves\{today}.csv'
isExist = os.path.exists(path)


st.title('Finance Tracker')
if st.button('Update Data'):
    if not isExist:
        st.write('Running Right Now')
        exec(open('Dashboard\Stock Screener\Join.py').read())
    else:
        st.write('Ran Today')
def Filter_df(sales,eps):
    df = pd.read_csv('Dashboard\Stock Screener\SAVE\Stocks Table.csv')
    #df = df.replace('-',np.nan)
    df = df[(df['Sales Q/Q %'] > sales)]  
    #df = df[(df['EPS this Y %'] > eps) | (df['EPS next Y %'] > eps)]
    df = df[(df['EPS this Y %'] > eps)]
    
    #df['EPS next Y %'] = df['EPS next Y %'].astype(float)
    df = df[(df['EPS next Y %'] > eps)]
    #MACD
    df = df.sort_values('Golden MACD',ascending= False)

    #Joing MTUM
    df = df[df['MTUM-MA-25'] > 100]
    df = df.sort_values(by = ['Golden MACD','MTUM-MA-25','EPS this Y %'],ascending= False)

    #Join Weekly MACD with MA
    df = df.sort_values('Weekly Golden MACD',ascending= False)
    df = df[df['Weekly Golden MACD'] <= df['Golden MACD']]
    st.write(len(df))
    st.dataframe(df)


df = pd.read_csv('Dashboard\Stock Screener\SAVE\Stocks Table.csv')


st.sidebar.header('Hello')
st.sidebar.multiselect('Sector',df['Sector'].unique())
#st.sidebar.multiselect('Industry',df['Industry'].unique())


sales = st.sidebar.number_input("Sales",value = 15)
eps = st.sidebar.number_input("EPS",value = 15)

Filter_df(sales,eps)
