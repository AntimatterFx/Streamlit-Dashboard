import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import openpyxl as xl

st.title('Networth Tracker')
wb = xl.load_workbook(r'Dashboard\Networth.xlsx',data_only=True) # data only so it doesnt read the formulas
#print(wb.sheetnames)
ws = wb['Summary Table'] #This is the only thing we care about 
df = pd.DataFrame(ws.values) #converts it into a df 

#Organizes the dataframe
df = df.set_index(df[0])
df = df[df.columns[2:]].T
df = df.set_index('Date')


##Makes the figure
fig = go.Figure()
df1 = df.drop(columns= ['Assets','Liabilities'],axis = 0) # Drops the columns you don't need for the graph

#To make the bars 
for col in df1[:-1].columns:
    if col == 'Net Worth': 
        fig.add_trace(go.Scatter(x = df.index,y = df[f'{col}'], name = col)) # Adds the Networth line
    else:
        fig.add_bar(x = df.index,y = df[f'{col}'], name = col) 
        
#Updates the figure 
fig.update_xaxes(title = 'Time') 
fig.update_yaxes(title = 'Cash') 

fig.update_layout(barmode='relative', title_text='Networth Tracker')
st.plotly_chart(fig)
st.dataframe(df)