import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import streamlit as st

#It shows the temperature of a specific city around time
def render():

    city = st.text_input("From what city do you want to know the average temperature? ")
    city = city.strip().title()                    #Format user input so the first char is upper as in the DB
    
    conn = sqlite3.connect("weather.db")
    query = f"SELECT AVG(temp) as avg_temp FROM weather WHERE city = '{city}';"
    df = pd.read_sql_query(query, conn)
    avg_temp = df.loc[0, "avg_temp"]      #Gets element 0 from avg_temp

    if avg_temp == None:
        conn.close()
        st.error("City not found")

    else:
        st.success(f"The average temperature of {city} is {round(avg_temp,2)}°C")

        #Plot of the temperatures recorded on that year
        query = f"SELECT DISTINCT date, city, temp FROM weather WHERE city = '{city}';"
        df = pd.read_sql_query(query, conn)
        #st.dataframe(df)  #Display dataframe

        fig, ax = plt.subplots()
        ax.plot(df["date"], df["temp"])
        ax.axhline(avg_temp, color="red", linestyle="--", label=f"Avg Temp ({avg_temp:.2f}°C)")

        for x,y in zip(df["date"], df["temp"]):
            ax.text(x, y, f"{y:.2f}", ha="center", va="bottom", fontsize=8)

        plt.xticks(rotation=90) 
        ax.set_xlabel("City") 
        ax.set_ylabel("Temperature (°C)") 
        ax.set_title(f"{city} temperatures around time") 
        plt.legend()
        plt.tight_layout() 
        st.pyplot(fig)
    
    conn.close()

render()
