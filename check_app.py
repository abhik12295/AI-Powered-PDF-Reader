import streamlit as st
from HOME import home_page
from pages.LOGIN import login_page
from pages.SIGNUP import signup_page
from pages.DASHBOARD import dashboard_page

# Initialize session state variables if they do not exist
if 'page' not in st.session_state:
    st.session_state.page = "HOME.py"  # Set default page to home

# Central page navigation logic based on session state
page = st.session_state.page

if page == "HOME":
    home_page()  # Show Home page
elif page == "pages/LOGIN":
    login_page()  # Show Login page
elif page == "pages/SIGNUP":
    signup_page()  # Show Sign Up page
elif page == "pages/DASHBOARD":
    dashboard_page()  # Show Dashboard page
