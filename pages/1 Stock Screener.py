#Dashboard\Main\Scripts\activate
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
st.title('Finance Tracker')
if st.button('Update Data'):
    exec(open('Dashboard\Stock Screener\Join.py').read())
    
def Filter_df(sales,eps):
    df = pd.read_csv('Dashboard\Stock Screener\SAVE\Stocks Table.csv')

    df = df[(df['Sales Q/Q %'] > sales)]  
    df = df[(df['EPS this Y %'] > eps) | (df['EPS next Y %'] > eps)]

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
st.sidebar.multiselect('Industry',df['Industry'].unique())


sales = st.sidebar.number_input("Sales",value = 15)
eps = st.sidebar.number_input("EPS this Year",value = 15)

Filter_df(sales,eps)
#eps__next_true =st.sidebar.number_input("EPS next Year",value = 15)
#eps__next_true =st.sidebar.number_input("EPS next Year",options = df['Sales Q/Q %'],default = 15)