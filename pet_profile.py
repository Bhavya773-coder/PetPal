import streamlit as st

def manage_pet_profile():
    st.header("Manage Your Pet's Profile")
    st.write("Create or update your pet's profile below.")
    
    pet_name = st.text_input("Pet's Name:")
    pet_breed = st.text_input("Pet's Breed:")
    pet_age = st.number_input("Pet's Age (years):", min_value=0)
    pet_size = st.selectbox("Pet's Size:", ["Small", "Medium", "Large"])
    
    if st.button("Save Profile"):
        if pet_name and pet_breed:
            pet_profile = {
                "name": pet_name,
                "breed": pet_breed,
                "age": pet_age,
                "size": pet_size
            }
            # Save pet profile (temporary storage using session_state)
            st.session_state.pet_profile = pet_profile
            st.success(f"Profile for {pet_name} saved!")
        else:
            st.warning("Please enter pet name and breed!")

    if "pet_profile" in st.session_state:
        st.write("Current Profile:", st.session_state.pet_profile)
