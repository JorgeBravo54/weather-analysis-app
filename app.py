import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Weather Analysis App", layout="centered")

conn = sqlite3.connect("weather.db")
columns = pd.read_sql_query("PRAGMA table_info(weather);", conn)

st.write("This is a page to compare temperatures and weather patterns between cities across the globe") 
st.write("This is the available information for each city")
st.write(columns) 

st.write("And this is a list of the cities available at the moment")
query = f"SELECT DISTINCT city FROM weather"
cities = pd.read_sql_query(query, conn)
st.write(cities)