import streamlit as st
import pandas as pd

def add_hostel(name, location, capacity, amenities):
    hostel = {
        'Name': name,
        'Location': location,
        'Capacity': capacity,
        'Amenities': amenities
    }
    if 'hostel_data' not in st.session_state:
        st.session_state['hostel_data'] = []
    st.session_state['hostel_data'].append(hostel)

def delete_hostel(index):
    if 'hostel_data' in st.session_state:
        st.session_state['hostel_data'].pop(index)

def main():
    st.title("Hostel Management App")
    
    menu = ["Add Hostel", "View Hostels"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Add Hostel":
        st.subheader("Add Hostel")
        
        with st.form("hostel_form"):
            name = st.text_input("Hostel Name")
            location = st.text_input("Location")
            capacity = st.number_input("Capacity", min_value=1)
            amenities = st.text_area("Amenities (comma-separated)")
            
            submit_button = st.form_submit_button(label='Add Hostel')
        
        if submit_button:
            add_hostel(name, location, capacity, amenities.split(','))
            st.success(f"Hostel '{name}' added successfully!")
    
    elif choice == "View Hostels":
        st.subheader("View Hostels")
        
        if 'hostel_data' in st.session_state and len(st.session_state['hostel_data']) > 0:
            df = pd.DataFrame(st.session_state['hostel_data'])
            st.dataframe(df)
            
            hostel_names = [hostel['Name'] for hostel in st.session_state['hostel_data']]
            selected_hostel = st.selectbox("Select a hostel to delete", hostel_names)
            delete_button = st.button("Delete Hostel")
            
            if delete_button:
                index_to_delete = hostel_names.index(selected_hostel)
                delete_hostel(index_to_delete)
                st.success(f"Hostel '{selected_hostel}' deleted successfully!")
        else:
            st.write("No hostels available. Please add some hostels.")

if __name__ == "__main__":
    main()

