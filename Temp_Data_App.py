# Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import streamlit as st

from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression

# Import Dataset
data = pd.read_csv("data.csv")

# Dataset Slicing
x = data.iloc[: , [3,5,6]]
y = data["Apparent Temperature (C)"]

# Dataset Slicing
x = data.iloc[: , [3,5,6]]
y = data.iloc[: , 4]

x_train, x_test, y_train, y_test = tts(x, y, test_size=0.3)

# Fit Regression
reg = LinearRegression()
reg.fit(x_train , y_train)

# Create Inputs
temprature = st.number_input("Temprature:")
wind_speed = st.number_input("Wind Speed:")
humidity = st.number_input("Humidity:")

# Create Prediction
pred = reg.predict([[temprature , humidity , wind_speed]])

# Show Predict
btn = st.button("Submit")

if(btn):
    st.success(f"Apparent Temperature: {pred}")
