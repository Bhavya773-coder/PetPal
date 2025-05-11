import streamlit as st

def reminder_system():
    st.header("Set Reminders for Your Pet")
    st.write("Get notified about your pet's vaccination, medication, and more.")
    
    reminder_type = st.selectbox("Select reminder type:", ["Vaccination", "Medication", "Check-up", "General Care"])
    reminder_date = st.date_input("Select reminder date")
    
    if st.button("Set Reminder"):
        reminder = {
            "type": reminder_type,
            "date": reminder_date
        }
        if "reminders" not in st.session_state:
            st.session_state.reminders = []
        st.session_state.reminders.append(reminder)
        st.success(f"Reminder for {reminder_type} set!")

    if "reminders" in st.session_state:
        st.write("Upcoming Reminders:", st.session_state.reminders)
