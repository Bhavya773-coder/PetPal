import streamlit as st
from chatbot_logic import get_bot_response
from pet_profile import manage_pet_profile
from health_tracker import health_tracker
from reminders import reminder_system
import random
import json

# Set page config
st.set_page_config(page_title="PetPal - Your Pet's Virtual Buddy", layout="centered")

# Main title and welcome
st.title("🐾 Welcome to PetPal - Your Pet's Virtual Companion 🐾")
st.subheader("Chat with PetPal for advice, reminders, and more!")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Home", "Chatbot", "Pet Profile", "Health Tracker", "Reminders", "Pet Tips"])

# Home page
if page == "Home":
    st.header("Welcome to PetPal!")
    st.write("PetPal is here to support you and your pet. You can interact with our chatbot, keep track of your pet's health, and much more!")
    st.image("assets/pet_image.jpg", caption="Your pet's virtual buddy!")
    st.write("Use the sidebar to explore the app.")

# Chatbot page
elif page == "Chatbot":
    st.header("Chat with PetPal")
    st.write("Ask me anything about your pet!")
    
    # Chatbot functionality
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", key="input")
    
    if user_input:
        response = get_bot_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("PetPal", response))
    
    # Display chat history
    for sender, msg in st.session_state.chat_history:
        st.write(f"**{sender}:** {msg}")

# Pet Profile page
elif page == "Pet Profile":
    manage_pet_profile()

# Health Tracker page
elif page == "Health Tracker":
    health_tracker()

# Reminders page
elif page == "Reminders":
    reminder_system()

# Pet Tips page
elif page == "Pet Tips":
    st.header("Pet Care Tips & Fun Facts")
    st.write("Here are some tips to take care of your pet!")

    # Random fun fact
    with open('data/pet_facts.json', 'r') as file:
        fun_facts = json.load(file)

    st.write("Fun Fact: " + random.choice(fun_facts["facts"]))

    # Health tips
    health_tips = [
        "Always keep fresh water available for your pet.",
        "Regular grooming helps maintain your pet's coat and skin.",
        "Watch for signs of stress in pets, such as excessive panting or withdrawal."
    ]
    st.write("Health Tip: " + random.choice(health_tips))
