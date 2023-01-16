import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text imput, slider, selecbox and subheader
st.title("Weather Forecast for the Next day")

place = st.text_input("Place: ")
days = st.slider('Forecast Days', min_value=1, max_value=5,
                help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")



if place:
    # Get the temperature / sky data
    filtered_data = get_data(place, days)

    if option == "Temperature":
        #       filtered_data = [float("{:.2f}".format(dic["main"]['temp'])) for dic in filtered_data]  - transforma em float com 2 casas dec
        temperatures = [dic["main"]['temp'] - 273.15 for dic in filtered_data]  # from Kelvin to celsius
        dates = [dic["dt_txt"] for dic in filtered_data]

        # Create a temperature plot -  Lib plotly or bokeh
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png","Snow":"images/snow.png"}
        sky_conditions = [dic["weather"][0]['main'] for dic in filtered_data]
        print(sky_conditions)
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths,width=115)
