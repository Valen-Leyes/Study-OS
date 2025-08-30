import requests
import streamlit as st

@st.cache_data
def check_availability(login_url, login_payload, url, string_to_search):
    # Create a session object
    session = requests.Session()

    # Send the login POST request
    response = session.post(login_url, data=login_payload)
    
    # Use the same session for the next request
    response = session.get(url)

    if string_to_search in response.text:
        return [string_to_search]
    else:
        return ['Hay mesas habilitadas', url]

# Streamlit component
def availability_checker(login_url, login_payload, url, string_to_search):
    if not login_url or not login_payload or not url or not string_to_search:
        st.error("No se proporcionaron todos los parámetros")
        return
    st.header('Check Availability')
    availability = check_availability(login_url, login_payload, url, string_to_search)
    st.write(availability[0])
    if availability[0] == 'Hay mesas habilitadas':
        st.write(availability[1])
