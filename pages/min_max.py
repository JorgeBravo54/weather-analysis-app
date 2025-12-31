import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import streamlit as st

#It shows the min vs max and average temp variation in each city
def render():

    st.title("Min Vs Max temperature") 
    st.write("This chart shows the minimum vs maximum temperatures recorded on each city.") 

    conn = sqlite3.connect("weather.db")
    query = f"SELECT city, AVG(temp) as avg, MIN(temp) as min, MAX(temp) as max, MAX(temp)-MIN(temp) as diff FROM weather GROUP BY city ORDER BY diff DESC;"
    df = pd.read_sql_query(query, conn)

    #Set up plot
    fig, ax = plt.subplots(figsize=(12,8))
    ax.vlines(df["city"], df["min"], df["max"], color="black")  #Lines to connect each dot by city
    ax.scatter(df["city"], df["min"], label="Min", color="#04C1F9")   #Scattered dots of each city min value
    ax.scatter(df["city"], df["max"], label="Max", color="#E31212")   #Dots of max value
    ax.scatter(df["city"], df["avg"], label="Avg", color="#65CE10")   #Dots of avg value
    ax.set_xlabel("City")
    ax.set_ylabel("Temperature")
    ax.set_title("Min-Max Temperature range per city")
    ax.legend()

    #Write each dot value
    for x,y in zip(df["city"], df["avg"]):
        ax.annotate(
            f"{y:.1f}",                    #Text
            (x,y),                         #Point to write the text of
            textcoords="offset points",    #Keep next to each point
            xytext=(-12.5,0),              # X,Y coords of the text
            ha="center",                   #Center
            fontsize=8,
            color="#65CE10",
            clip_on=False                  #Stop axes from being cut off in case they go out of the figure
        )

    for x,y in zip(df["city"], df["min"]):
        ax.annotate(
            f"{y:.1f}",                   
            (x,y),                        
            textcoords="offset points",   
            xytext=(0,-12),              
            ha="center",                  
            fontsize=8,
            color="#04C1F9",
            clip_on=False                 
        )

    for x,y in zip(df["city"], df["max"]):
        ax.annotate(
            f"{y:.1f}",                
            (x,y),                        
            textcoords="offset points",   
            xytext=(0,5),             
            ha="center",                  
            fontsize=8,
            color="#E31212",
            clip_on=False                
        )

    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot(fig)
    conn.close()

render()