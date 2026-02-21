import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("🚀 Rocket Thrust Prediction")

time = st.number_input("Time")
altitude = st.number_input("Altitude")
velocity = st.number_input("Velocity")
mass = st.number_input("Mass")

if st.button("Predict"):
    input_data = pd.DataFrame([[time, altitude, velocity, mass]],
                             columns=['Time','Altitude','Velocity','Mass'])
    
    result = model.predict(input_data)
    st.success(f"Predicted Thrust: {result[0]:.2f}")