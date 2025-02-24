import json
import streamlit as st
import pandas as pd
import altair as alt

# Load the JSON data from the file
with open('weather.json', 'r') as f:
    weather_data = json.load(f)

# Extract temperature data
temperature_data = weather_data["temperature"]["data"]

# Convert to DataFrame
df = pd.DataFrame(temperature_data)

# Sidebar for location selection
location = st.sidebar.selectbox("Select a location", df["place"])

# Display bar chart of all locations
st.title("Temperature of All Locations")
chart = alt.Chart(df).mark_bar().encode(
    x='place',
    y='value',
    tooltip=['place', 'value']
).properties(
    width=800,
    height=400
)
st.altair_chart(chart, use_container_width=True)

# Display selected location temperature
st.title(f"Temperature at {location}")
selected_temp = df[df["place"] == location]["value"].values[0]
st.write(f"The temperature at {location} is {selected_temp}°C")