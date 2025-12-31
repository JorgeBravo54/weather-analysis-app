
import sqlite3
import requests
import streamlit as st
api_key = 'e2cc7a370faee5d1798fd0d465c01353'

#Insert values to the DB
def render():

    st.title("Add a row to the database") 
    st.write("Write the city you would like to add to the database.") 

    from datetime import date
    city = st.text_input("Write the name of the city you wish to add")
    city = city.strip().title()  
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}")

    if weather_data.json()['cod'] == '404':
        st.error("City not found")
    else:

        #print(weather_data.json())
        date = date.today()
        city = weather_data.json()['name']
        longitude = weather_data.json()['coord']['lon']
        latitude = weather_data.json()['coord']['lat']
        weather = weather_data.json()['weather'][0]['main']
        weather_description = weather_data.json()['weather'][0]['description']
        sea_level = weather_data.json()['main']['sea_level']
        temp = weather_data.json()['main']['temp']

        st.write("Adding...")

        conn = sqlite3.connect("weather.db")
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO weather (
            date, city, temp, longitude, latitude, weather, weather_description, sea_level
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            date,
            city,
            temp,
            longitude,
            latitude,
            weather,
            weather_description,
            sea_level
        ))
        conn.commit()
        conn.close()
        st.success("Values added to the database correctly and connection closed")

render()