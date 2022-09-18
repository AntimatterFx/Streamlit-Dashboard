# ---- Modules ------- 
import streamlit as st
import pandas as pd
import plotly.express as px
st.header("Fruits List")
# ---- Creating Dictionary ----
_dic = { 'Name': ['Mango', 'Apple', 'Banana'],
         'Quantity': [45, 38, 90]}
_df = pd.DataFrame(_dic)
def add(x,y):
    return x+y
load = st.button('Load Data')
load2 = st.button('Load Data2')
if 'load_state' not in st.session_state:
    st.session_state['load_state'] = False
    st.session_state['load_state2'] = False
if load or st.session_state['load_state']:
    st.write(_df)
    x = st.number_input('X')
    y = st.number_input('Y')
    if load2 or st.session_state['load_state2']:
        z = add(x,y)
        
   # ---- Plot types -------
opt = st.radio('Plot type :',['Bar', 'Pie'])
if opt == 'Bar':
    fig = px.bar(_df, x= 'Name',
                y = 'Quantity',title ='Bar Chart')
    st.plotly_chart(fig)
   
else:     
    fig = px.pie(_df,names = 'Name',
                values = 'Quantity',title ='Pie Chart')
    st.plotly_chart(fig)