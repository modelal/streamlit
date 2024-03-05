import streamlit as st
import src.manage_data as cleaning
import plotly.express as px
import codecs
import streamlit.components.v1 as components


# 1. Create a barchart
st.write("""
#ploting page""")

data_bar = cleaning.bar_1()
st.bar_chart(data_bar)

#insert a selecction box with two options(drop-down menu)
#person = st.selectbox("Choose one character", ["finn", "jake"]) #selected characters

df = cleaning.load_dataframe()
characters = list(df["character_name"].unique()) # all the characters
person = st.selectbox("Choose one character", characters)

#filters de data given a caracter(person)
data_for_plot = cleaning.graph(person)

#include the figure:
fig = px.line(data_for_plot, y="polarity")
st.plotly_chart(fig)

# Insert a tableau MAP
f = codecs.open("data/tableau.html", "r")
tableau = f.read()

#display
components.html(tableau, height=500, scrolling=True)