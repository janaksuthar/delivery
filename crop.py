import streamlit as st
import pickle
import pandas as pd

# Load the trained model
filename = r"crop_recommendation_model.sav"
loaded_model = pickle.load(open(filename, 'rb'))

# Create a title for the app
st.title("Crop Recommendation System")

# Get input from the user
N = st.number_input("Nitrogen", min_value=0, max_value=100)
P = st.number_input("Phosphorus", min_value=0, max_value=100)
K = st.number_input("Potassium", min_value=0, max_value=100)
temperature = st.number_input("Temperature", min_value=0.0, max_value=100.0)
humidity = st.number_input("Humidity", min_value=0.0, max_value=100.0)
ph = st.number_input("pH", min_value=0.0, max_value=14.0)
rainfall = st.number_input("Rainfall", min_value=0.0, max_value=1000.0)

# Create a button to make predictions
if st.button("Predict Crop"):
  # Prepare the input data
  input_data = [[N, P, K, temperature, humidity, ph, rainfall]]

  # Make predictions
  prediction = loaded_model.predict(input_data)

  # Display the prediction
  st.success(f"The recommended crop is: {prediction[0]}")
