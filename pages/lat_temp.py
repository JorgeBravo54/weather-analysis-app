import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import streamlit as st

def render():

    st.title("Relation between latitude and temperature") 
    st.write("This chart shows each city latitude, temperature range and the correlation between them.") 

    conn = sqlite3.connect("weather.db")
    query = f"SELECT city, ABS(latitude) as latitude, MAX(temp) - MIN(temp) as temp_range FROM WEATHER GROUP BY city, latitude;"
    df = pd.read_sql_query(query, conn)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(
        df["latitude"],
        df["temp_range"]
    )

    correlation = df["latitude"].corr(df["temp_range"])
    ax.set_xlabel("Absolute Latitude (°)")
    ax.set_ylabel("Temperature Range(°C)")
    ax.set_title(f"Temperature Range vs Latitude\nCorrelation: {correlation:.2f}")
    
    plt.tight_layout()
    st.pyplot(fig)
    conn.close()

render()
    