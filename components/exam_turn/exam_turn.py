import requests
import streamlit as st

@st.cache_data
def check_availability(login_url, login_payload, url, string_to_search):
    # Create a session object
    session = requests.Session()

    # Send the login POST request
    response = session.post(login_url, data=login_payload)

    # Get the session cookie value from the response
    session_cookie_value = session.cookies.get("siu_sess__g3w_des01")

    # Send the request to the target URL using the session cookie
    cookies = {"siu_sess__g3w_des01": session_cookie_value}
    response = requests.get(url, cookies=cookies)

    if string_to_search in response.text:
        return [string_to_search]
    else:
        return ['Hay mesas habilitadas', url]

# Streamlit component
def availability_checker(login_url, login_payload, url, string_to_search):
    st.header('Check Availability')
    availability = check_availability(login_url, login_payload, url, string_to_search)
    st.write(availability[0])
    if availability[0] == 'Hay mesas habilitadas':
        st.write(availability[1])
