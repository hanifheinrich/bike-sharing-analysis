import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("day_clean.csv")

st.title("Bike Sharing Dashboard")

#Layouting Baris 1
date_range = st.date_input(
    "Pilih rentang tanggal:",
    value=[pd.to_datetime(df["dteday"].min()), pd.to_datetime(df["dteday"].max())]
)

if len(date_range) == 2:
    start_date, end_date = date_range
    df = df[(pd.to_datetime(df["dteday"]) >= pd.to_datetime(start_date)) & (pd.to_datetime(df["dteday"]) <= pd.to_datetime(end_date))]

#Layouting Baris 2
line_chart1 = px.line(
    df,
    x="dteday",
    y=["casual", "registered"],
    labels={"value": "Count", "variable": "User Type"},
    title="Casual User vs Registered User"
)
st.plotly_chart(line_chart1, use_container_width=True)

#Layouting Baris 3
col1, col2, col3 = st.columns(3)

with col1:
    donut_season = px.pie(
        df,
        names="season",
        values="count_cr",
        title="Perbandingan User berdasarkan Musim",
        hole=0.3
    )
    donut_season.update_layout(
        legend=dict(
            x=0.5, 
            y=0.5,  
            orientation="h",  
            xanchor="center",  
            yanchor="middle", 
        ),
        margin=dict(t=40, b=0, l=0, r=0), 
    )
    st.plotly_chart(donut_season)

with col2:
    donut_humidity = px.pie(
        df,
        names="humidity_category",
        values="count_cr",
        title="Perbandingan User berdasarkan Kelembapan",
        hole=0.3
    )
    donut_humidity.update_layout(
        legend=dict(
            x=0.5,  
            y=0.5,  
            orientation="h",  
            xanchor="center",  
            yanchor="middle", 
        ),
        margin=dict(t=40, b=0, l=0, r=0),  
    )
    st.plotly_chart(donut_humidity)

with col3:
    donut_category_days = px.pie(
        df,
        names="category_days",
        values="count_cr",
        title="User Weekend vs Weekday",
        hole=0.3
    )
    donut_category_days.update_layout(
        legend=dict(
            x=0.5,  
            y=0.5,  
            orientation="h",  
            xanchor="center",  
            yanchor="middle", 
        ),
        margin=dict(t=40, b=0, l=0, r=0), 
    )
    st.plotly_chart(donut_category_days)

#Layouting Baris 4
col1, col2 = st.columns(2)

with col1:
    donut_holiday = px.pie(
        df,
        names="holiday",
        values="count_cr",
        title="User Holiday vs No Holiday",
        hole=0.3
    )
    donut_holiday.update_layout(
        legend=dict(
            x=0.5, 
            y=0.5, 
            orientation="h", 
            xanchor="center", 
            yanchor="middle", 
        ),
        margin=dict(t=40, b=0, l=0, r=0), 
    )
    st.plotly_chart(donut_holiday)

with col2:
    donut_weather_situation = px.pie(
        df,
        names="weather_situation", 
        values="count_cr",  
        title="Perbandingan User berdasarkan Cuaca",
        hole=0.3
    )
    donut_weather_situation.update_layout(
        legend=dict(
            x=0.5,  
            y=0.5, 
            orientation="h", 
            xanchor="center",  
            yanchor="middle",  
        ),
        margin=dict(t=40, b=0, l=0, r=0), 
    )
    st.plotly_chart(donut_weather_situation)

#Layouting Baris 5
st.write("## Preview Data")
st.dataframe(df, use_container_width=True)
