import streamlit as st
import pandas as pd

# Function to classify health data
def classify_health(heart_rate, bp, temp, spo2):
    classification = {}

    # Normal ranges
    if 60 <= heart_rate <= 100:
        classification["Heart Rate"] = "Normal ✅"
    elif heart_rate < 60:
        classification["Heart Rate"] = "Low ❗"
    else:
        classification["Heart Rate"] = "High ⚠️"

    if 90 <= bp <= 120:
        classification["Blood Pressure"] = "Normal ✅"
    elif bp < 90:
        classification["Blood Pressure"] = "Low ❗"
    else:
        classification["Blood Pressure"] = "High ⚠️"

    if 36.1 <= temp <= 37.2:
        classification["Temperature"] = "Normal ✅"
    elif temp < 36.1:
        classification["Temperature"] = "Low ❗"
    else:
        classification["Temperature"] = "High ⚠️"

    if spo2 >= 95:
        classification["SpO2"] = "Normal ✅"
    else:
        classification["SpO2"] = "Low ❗"

    return classification

# Streamlit UI
st.title("Health Data Monitor 🚑")

heart_rate = st.number_input("Enter Heart Rate (bpm):", min_value=30, max_value=200, value=75)
bp = st.number_input("Enter Blood Pressure (mmHg):", min_value=50, max_value=200, value=110)
temp = st.number_input("Enter Temperature (°C):", min_value=30.0, max_value=42.0, value=36.5)
spo2 = st.number_input("Enter SpO2 (%):", min_value=50, max_value=100, value=98)

if st.button("Check Health Status"):
    result = classify_health(heart_rate, bp, temp, spo2)
    st.write("### Health Analysis:")
    for key, value in result.items():
        st.write(f"**{key}:** {value}")
