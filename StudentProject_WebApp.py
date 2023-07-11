import streamlit as st
import plotly.express as px
import pandas
import sqlite3

database_name = "temp_db.db"
connection = sqlite3.connect(database_name)
cursor = connection.cursor()
cursor.execute("SELECT * FROM temps")
alldata = cursor.fetchall()

df = pandas.DataFrame(alldata, columns=['date_unix','temperature'])

figure = px.line(x=df["date_unix"], y=df["temperature"],
                             labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)