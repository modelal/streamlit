import streamlit as st

#import functions from src
#folder.file
import src.manage_data as cleaning

df = cleaning.load_dataframe()

st.write("Adventures time data")

st.dataframe(df)