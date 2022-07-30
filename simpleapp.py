import streamlit as st 
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import plotly_express as px


st.set_page_config(layout="wide")
st.image('logo.png', width=100)
with st.sidebar:
    select = option_menu(
        menu_title='Model Selection',
        options= ['TATA', 'AL'],
        icons = ['truck','truck'],
        menu_icon='truck-flatbed'
    )
   
col2, col3= st.columns([1.2,0.2])



with col2:
    st.title('Hyper Automotives')
    st.caption('Innovative Solution')

    st.header('building an automotive future'.capitalize())
    #SubHeader
    st.subheader('Reducing Global automobile emissions & hastening the electrification of vehicles.!'.capitalize())
    def interactiveplots(df):
        comp = st.selectbox('Select to See Report Comparision', 
        options=['Injector','Railing', 'ECU'])
        if comp == 'Injector':
            plot = px.line(df, x=df['iq'],y=df['iq_pred'], title='Fuel Injection Compared')
            plot.show()      
    if select == 'TATA':
        st.image('./Component Images/Background MH 12 PQ 5841.png', caption='Model-TATA 5841', width= 750)
        df = pd.read_csv('AB 12 BC 3456.csv')
        grph = option_menu(
        menu_title='Visualize',
        options= ['Interactive Graph', 'Sample data'],
        icons = ['graph-up-arrow','clipboard-data'],
        menu_icon='activity',
        orientation='horizontal'
    )
        if grph == 'Interactive Graph':
            x = interactiveplots(df)
            x
        if grph == 'Sample data':
            y = df.sample(10)
            y
    if select == 'AL':
        st.image('./Component Images/Background TN 34 AB 7345.png', caption='Model-AL 7345', width= 750)
        df = pd.read_csv('BC 12 CD 3456.csv')
        grph = option_menu(
        menu_title='Visualize',
        options= ['Interactive Graph', 'Sample data'],
        icons = ['graph-up-arrow','clipboard-data'],
        menu_icon='activity',
        orientation='horizontal'
    )
        if grph == 'Interactive Graph':
            x = df.head()
            x
        if grph == 'Sample data':
            y = df.sample(10)
            y

df = pd.read_csv('vehicle_list.csv')
st.dataframe(data=df, width=200)