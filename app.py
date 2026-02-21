import streamlit as st
import numpy as np
import pickle

st.title("🚀 Rocket Prediction App")

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.write("Enter Values")

time = st.number_input("Time")
altitude = st.number_input("Altitude")
velocity = st.number_input("Velocity")
mass = st.number_input("Mass")

input_data = np.array([[time, altitude, velocity, mass]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Thrust: {prediction[0]}")