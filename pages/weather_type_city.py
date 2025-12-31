import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import streamlit as st

#It shows the frequency of each weather type of a specific city
def render():

    #Format user input
    city = st.text_input("From what city do you want to know the most common weather types? ")
    city = city.strip().title()   

    conn = sqlite3.connect("weather.db")
    query = f"SELECT city, weather, COUNT(*) as count FROM weather WHERE city='{city}' GROUP BY city, weather;"
    df = pd.read_sql_query(query, conn)

    if df.empty:
        conn.close()
        st.error("City not found")
    else:
        st.success(f"Most common weather types of {city}")

        fig, ax = plt.subplots()
        ax.pie(
            df["count"],
            labels=df["weather"],
            autopct="%1.1f%%",
            startangle=90
        )
        ax.set_title(f"Weather frequency in {city}")
        plt.tight_layout()
        st.pyplot(fig)

render()