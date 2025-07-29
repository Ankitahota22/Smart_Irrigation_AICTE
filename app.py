import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("Farm_Irrigation_System.pkl")

# Page configuration
st.set_page_config(page_title="Smart Sprinkler System", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 2rem;
        }
        .title {
            color: #2c3e50;
            text-align: center;
        }
        .footer {
            margin-top: 3rem;
            text-align: center;
            color: #888;
        }
        .status-on {
            background-color: #2ecc71;
            color: white;
            padding: 0.4rem 0.8rem;
            border-radius: 10px;
            display: inline-block;
        }
        .status-off {
            background-color: #e74c3c;
            color: white;
            padding: 0.4rem 0.8rem;
            border-radius: 10px;
            display: inline-block;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown("<h1 class='title'>🌿 Smart Sprinkler System</h1>", unsafe_allow_html=True)
st.subheader("Predict whether each sprinkler should be ON or OFF based on sensor inputs.")
st.write("Adjust the **20 sensor sliders** (values scaled between 0 and 1) and click **Predict Sprinklers**.")

# Sensor input sliders in columns (2 per row)
sensor_values = []
cols = st.columns(2)
for i in range(20):
    with cols[i % 2]:
        val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        sensor_values.append(val)

# Prediction button
if st.button("🚀 Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("### 🔍 Prediction Result:")
    for i, status in enumerate(prediction):
        badge = f"<span class='status-on'>ON</span>" if status == 1 else f"<span class='status-off'>OFF</span>"
        st.markdown(f"**Sprinkler {i} (parcel_{i})**: {badge}", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Created by a beginner developer 🌱</div>", unsafe_allow_html=True)
