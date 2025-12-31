import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import streamlit as st

#Shows a comparison between the avg temp of every city in the db
def render():

    st.title("🌡️ City-to-City Temperature Comparison") 
    st.write("This chart shows the average temperature per city from the weather database.") 

    conn = sqlite3.connect("weather.db")
    query = f"SELECT city, AVG(temp) as avg_temp FROM WEATHER GROUP BY city ORDER BY avg_temp DESC;"
    df = pd.read_sql_query(query, conn)

    #Plot 
    fig, ax = plt.subplots()
    ax.plot(df["city"], df["avg_temp"])

    #Label each point
    for x,y in zip(df["city"], df["avg_temp"]):
        ax.text(x ,y ,f"{y:.2f}", ha="center", va="bottom", fontsize=6, rotation=20)

    plt.xticks(rotation=90)
    ax.set_xlabel("Cities")
    ax.set_ylabel("Avg Temperatures")
    ax.set_title("Cities temperature comparison")
    
    st.pyplot(fig)
    
    conn.close()

render()