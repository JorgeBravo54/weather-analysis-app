import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import streamlit as st

#Shows the frequency of each weather type per city
def render():

    st.title("Most common weather types per city") 
    st.write("This chart shows the most common weather types on each city from the weather database.") 

    conn = sqlite3.connect("weather.db")
    query = f"SELECT city, weather, COUNT(*) as count FROM weather GROUP BY city, weather;"
    df = pd.read_sql_query(query, conn)

    pivot = df.pivot_table( index="city", columns="weather", values="count", aggfunc="sum", fill_value=0 )

    fig, ax = plt.subplots(figsize=(10,5))

    pivot.plot(kind="bar", stacked=True, colormap="tab20", ax=ax)

    ax.set_title("Weather counts by city")
    ax.set_xlabel("City")
    ax.set_ylabel("Count")
    ax.legend(title="Weather", bbox_to_anchor=(1.02,1)) #Legend box outside the figure

    plt.tight_layout()
    st.pyplot(fig)

render()