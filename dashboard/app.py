import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import os

st.set_page_config(page_title="AI Maintenance UI", layout="wide")
st.title("🏭 AI-Powered Predictive Maintenance")

MODEL_PATH = 'models/predictive_model.pkl'
DATA_PATH = 'data/sensor_telemetry.csv'

if not os.path.exists(MODEL_PATH) or not os.path.exists(DATA_PATH):
    st.error("⚠️ System Offline: Run `simulate_sensors.py` and `train_model.py` first.")
    st.stop()

model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH)

st.sidebar.header("Virtual Sensor Input")
t = st.sidebar.slider("Temperature (°C)", 20.0, 80.0, 45.0)
v = st.sidebar.slider("Vibration (mm/s)", 0.0, 10.0, 2.5)
c = st.sidebar.slider("Current (A)", 0.0, 20.0, 10.0)

# Real-Time Prediction Logic
prediction = model.predict([[t, v, c]])[0]
if prediction == 1:
    st.error("⚠️ ALERT: High Probability of Impending Machine Failure Detected!")
else:
    st.success("✅ Machine Operating within Normal Parameters.")

st.subheader("Recent Sensor Telemetry (Virtual Fleet)")
chart_data = df.tail(100).reset_index()

# Plotly chart matching your requested "Temp & Vibration Trends" layout
fig = px.line(
    chart_data, 
    x='index', 
    y=['temperature', 'vibration'], 
    title="Temp & Vibration Trends",
    labels={"value": "value", "variable": "variable", "index": "index"}
)
st.plotly_chart(fig, use_container_width=True)