import streamlit as st 
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu


st.set_page_config(layout="wide")
st.image('logo.png', width=100)

#st.write(f'Streamlit Version = {(st.__version__)}')

col2, col3 = st.columns([1.2,0.2])

with st.sidebar:
    select = option_menu(
        menu_title='Model Selection',
        options= ['TATA', 'AL']
    )

with col2:
    st.title('Hyper Automotives')
    st.caption('Innovative Solution')

    st.header('building an automotive future'.capitalize())
    #SubHeader
    st.subheader('Reducing Global automobile emissions & hastening the electrification of vehicles.!'.capitalize())
    if select == 'TATA':
        st.image('./Component Images/Background MH 12 PQ 5841.png', caption='Model-TATA 5841', width= 750)
    if select == 'AL':
        st.image('./Component Images/Background TN 34 AB 7345.png', caption='Model-AL 7345', width= 750)
        
with col3:
    df = pd.read_csv('vehicle_list.csv')
    st.dataframe(data=df, width=200)