import streamlit as st
import os
from supabase import Client, create_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Ensure set_page_config is the first Streamlit command
st.set_page_config(page_title="🔐 Welcome!", layout="centered", initial_sidebar_state='collapsed')

st.title("📄 AI PDF Assistant")

# if 'user' in st.session_state:
#     del st.session_state["user"]

def logout():
    """Logout user and reset session state."""
    st.session_state.user = None
    st.session_state.page = "HOME.py"
    st.rerun()

def home_page():
    if 'user' not in st.session_state:
            st.session_state.user = None
            #st.session_state.page = "HOME.py"

    user = st.session_state.user
    print(user)
    if user and 'email' in user:
        with st.expander('User Information'):
            st.success(f'🎉 Logged in as: {user.email}')
            if hasattr(user, 'user_metadata') and 'full_name' in user.user_metadata:
                st.write(f'Username: {user.user_metadata["email"]}') 


        if st.button("Go to Dashboard"):
            st.session_state.page = "DASHBOARD.py"
            st.rerun()

        if st.button("Logout"):
            logout()
            
    else:
        st.info("Please log in or sign up to continue.")
        col1, col2 = st.columns(2)
        
        with col1:
            login_disabled = user is not None  # Disable Login if user is logged in
            st.button("Login", disabled=login_disabled, on_click=lambda: set_page("LOGIN.py"))
            # if st.button("Login"):
            #     st.session_state.page = "LOGIN.py"
            #     st.rerun()

        with col2:
            signup_disabled = user is not None  # Disable Sign Up if user is logged in
            st.button("Sign Up", disabled=signup_disabled, on_click=lambda: set_page("SIGNUP.py"))
            # if st.button("Sign Up"):
            #     st.session_state.page = "SIGNUP.py"
            #     st.rerun()

def set_page(page_name):
    """Helper function to change page state and rerun the app."""
    st.session_state.page = page_name
    #st.rerun()

# # Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "HOME.py"

# Page routing
if st.session_state.page == "HOME.py":
    home_page()
    
elif st.session_state.page == "LOGIN.py":
    from pages.LOGIN import login_page
    login_page()

elif st.session_state.page == "SIGNUP.py":
    from pages.SIGNUP import signup_page
    signup_page()

elif st.session_state.page == "DASHBOARD.py":  # Fixed typo
    from pages.DASHBOARD import dashboard_page
    dashboard_page()