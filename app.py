import streamlit as st
import pandas as pd
name='Jungu Lee'
st.text(f'My name is {name}')

st.markdown('This is **markdown**')

df=pd.read_csv('iris.csv')

st.dataframe(df)