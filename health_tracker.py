import json
import streamlit as st

def health_tracker():
    st.header("Track Your Pet's Health")
    st.write("Log your pet's health metrics to stay on top of their well-being.")
    
    weight = st.number_input("Pet's Weight (kg):", min_value=0.0, format="%.2f")
    appetite = st.selectbox("Appetite:", ["Good", "Fair", "Poor"])
    mood = st.selectbox("Mood:", ["Happy", "Neutral", "Sad"])
    stool_quality = st.selectbox("Stool Quality:", ["Normal", "Loose", "Hard"])

    if st.button("Save Health Log"):
        health_data = {
            "weight": weight,
            "appetite": appetite,
            "mood": mood,
            "stool_quality": stool_quality
        }
        # Save health log (temporary storage using session_state)
        if "health_logs" not in st.session_state:
            st.session_state.health_logs = []
        st.session_state.health_logs.append(health_data)
        st.success("Health log saved!")

    if "health_logs" in st.session_state:
        st.write("Health Logs:", st.session_state.health_logs)
