import streamlit as st
import random
import time

# Page settings
st.set_page_config(page_title="Smart Home", layout="centered")

# Title
st.title("🏠 Smart Home Simulation")

# Light Control
st.subheader("💡 Light Control")
light = st.toggle("Turn Light ON/OFF")

if light:
    st.success("Light is ON 💡")
else:
    st.error("Light is OFF ❌")

# Temperature Sensor (auto-refresh style)
st.subheader("🌡 Temperature Sensor")
temperature = random.randint(20, 35)
st.info(f"Current Temperature: {temperature} °C")

# Fan Control
st.subheader("🌀 Fan Control")
fan_speed = st.slider("Select Fan Speed", 0, 3)

if fan_speed == 0:
    st.write("Fan is OFF")
elif fan_speed == 1:
    st.write("Fan Speed: Low")
elif fan_speed == 2:
    st.write("Fan Speed: Medium")
else:
    st.write("Fan Speed: High")

# Device Status Panel
st.subheader("📊 Device Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Light", "ON" if light else "OFF")

with col2:
    st.metric("Fan Speed", fan_speed)

with col3:
    st.metric("Temperature", f"{temperature}°C")

# Auto-refresh button
if st.button("🔄 Refresh Data"):
    st.experimental_rerun()
