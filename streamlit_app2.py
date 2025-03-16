import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to classify health data
def classify_health(heart_rate, bp, temp, spo2):
    classification = {}

    if 60 <= heart_rate <= 100:
        classification["Heart Rate"] = "✅ Normal"
    elif heart_rate < 60:
        classification["Heart Rate"] = "🔵 Low"
    else:
        classification["Heart Rate"] = "🔴 High"

    if 90 <= bp <= 120:
        classification["Blood Pressure"] = "✅ Normal"
    elif bp < 90:
        classification["Blood Pressure"] = "🔵 Low"
    else:
        classification["Blood Pressure"] = "🔴 High"

    if 36.1 <= temp <= 37.2:
        classification["Temperature"] = "✅ Normal"
    elif temp < 36.1:
        classification["Temperature"] = "🔵 Low"
    else:
        classification["Temperature"] = "🔴 High"

    if spo2 >= 95:
        classification["SpO2"] = "✅ Normal"
    else:
        classification["SpO2"] = "🔴 Low"

    return classification

# Streamlit UI
st.set_page_config(page_title="Health Monitor", page_icon="🚑", layout="wide")

st.title("🚑 Health Data Monitor")
st.write("Enter your health data and check if it's within a normal range.")

# Organize inputs into two columns
col1, col2 = st.columns(2)

with col1:
    heart_rate = st.slider("💓 Heart Rate (bpm)", 30, 200, 75)
    temp = st.slider("🌡️ Temperature (°C)", 30.0, 42.0, 36.5)

with col2:
    bp = st.slider("🩸 Blood Pressure (mmHg)", 50, 200, 110)
    spo2 = st.slider("🫁 SpO2 (%)", 50, 100, 98)

# Display health classification
st.subheader("🔍 Health Analysis:")
result = classify_health(heart_rate, bp, temp, spo2)
for key, value in result.items():
    st.write(f"**{key}:** {value}")

# Display chart visualization
st.subheader("📊 Health Data Overview")

data = {"Heart Rate": heart_rate, "Blood Pressure": bp, "Temperature": temp, "SpO2": spo2}
labels, values = list(data.keys()), list(data.values())

# Reduce figure size
fig, ax = plt.subplots(figsize=(4, 2))  # Adjusted size

ax.barh(labels, values, color=['blue', 'red', 'green', 'purple'])
ax.set_xlim(0, max(values) + 10)  # Dynamic axis scaling

st.pyplot(fig)

# Custom Styling
st.markdown(
    """
    <style>
        .main {
            background-color: #f5f5f5;
        }
        h1 {
            color: #1f77b4;
        }
    </style>
    """,
    unsafe_allow_html=True
)
