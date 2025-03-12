# import streamlit as st
# import os
# from supabase import Client, create_client
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()
# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# # Ensure set_page_config is the first Streamlit command
# st.set_page_config(page_title="🔐 Welcome!", layout="centered", initial_sidebar_state='collapsed')

# st.title("📄 AI PDF Assistant")

# # if 'user' in st.session_state:
# #     del st.session_state["user"]

# def logout():
#     """Logout user and reset session state."""
#     st.session_state.user = None
#     st.session_state.page = "HOME.py"
#     st.rerun()

# def home_page():
#     if 'user' not in st.session_state:
#             st.session_state.user = None
#             #st.session_state.page = "HOME.py"

#     user = st.session_state.user
#     print(user)
#     if user and 'email' in user:
#         with st.expander('User Information'):
#             st.success(f'🎉 Logged in as: {user.email}')
#             if hasattr(user, 'user_metadata') and 'full_name' in user.user_metadata:
#                 st.write(f'Username: {user.user_metadata["email"]}') 

#         if st.button("Go to Dashboard"):
#             # st.session_state.page = "DASHBOARD.py"
#             # st.rerun()
#             st.switch_page("pages/DASHBOARD.py")

#         if st.button("Logout"):
#             logout()
            
#     else:
#         st.info("Please log in or sign up to continue.")
#         col1, col2 = st.columns(2)
        
#         with col1:
#             login_disabled = user is not None  # Disable Login if user is logged in
#             st.button("Login", disabled=login_disabled, on_click=lambda: set_page("LOGIN.py"))
#             # if st.button("Login"):
#             #     st.session_state.page = "LOGIN.py"
#             #     st.rerun()

#         with col2:
#             signup_disabled = user is not None  # Disable Sign Up if user is logged in
#             st.button("Sign Up", disabled=signup_disabled, on_click=lambda: set_page("SIGNUP.py"))
#             # if st.button("Sign Up"):
#             #     st.session_state.page = "SIGNUP.py"
#             #     st.rerun()

# def set_page(page_name):
#     """Helper function to change page state and rerun the app."""
#     st.session_state.page = page_name
#     #st.rerun()

# # # Initialize session state
# if "page" not in st.session_state:
#     st.session_state.page = "HOME.py"

# # Page routing
# if st.session_state.page == "HOME.py":
#     home_page()
    
# elif st.session_state.page == "LOGIN.py":
#     from pages.LOGIN import login_page
#     login_page()

# elif st.session_state.page == "SIGNUP.py":
#     from pages.SIGNUP import signup_page
#     signup_page()

# elif st.session_state.page == "DASHBOARD.py":  # Fixed typo
#     from pages.DASHBOARD import dashboard_page
#     dashboard_page()


####perfect###

# import streamlit as st
# import os
# from supabase import Client, create_client
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()
# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# # Ensure set_page_config is the first Streamlit command
# st.set_page_config(page_title="🔐 Welcome!", layout="centered", initial_sidebar_state='collapsed')

# st.title("📄 AI PDF Assistant")

# def logout():
#     """Logout user and reset session state."""
#     st.session_state.user = None
#     st.rerun()

# def home_page():
#     """Static Home Page with Login and Signup Redirection"""

#     if "user" not in st.session_state:
#         st.session_state.user = None

#     user = st.session_state.user

#     if user:
#         st.success(f'🎉 Logged in as: {user.email}')
#         if st.button("Go to Dashboard"):
#             st.switch_page("pages/DASHBOARD.py")
#         if st.button("Logout"):
#             logout()
    
#     else:
#         st.info("Please log in or sign up to continue.")

#         col1, col2 = st.columns(2)

#         with col1:
#             if st.button("Login"):
#                 st.switch_page("pages/LOGIN.py")

#         with col2:
#             if st.button("Sign Up"):
#                 st.switch_page("pages/SIGNUP.py")

# # Show the home page
# home_page()


import streamlit as st
import os
from supabase import Client, create_client
from dotenv import load_dotenv
from streamlit_lottie import st_lottie
import json
import requests

# Load environment variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Ensure set_page_config is the first Streamlit command
st.set_page_config(page_title="🔐 Welcome!", layout="centered", initial_sidebar_state='collapsed')

st.title("📑 AI PDF Assistant")

# Load Lottie animation
lottie_url = "https://lottie.host/5950fc8d-9bd3-413b-8c38-e93ae7b6af6b/Tw2m4YoabM.json"  # Replace with a relevant PDF animation

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation = load_lottieurl(lottie_url)


def logout():
    """Logout user and reset session state."""
    st.session_state.user = None
    st.rerun()


def home_page():
    """Static Home Page with Login and Signup Redirection"""
    
    if "user" not in st.session_state:
        st.session_state.user = None
    
    user = st.session_state.user
    
    # Display animation
    if lottie_animation:
        st_lottie(lottie_animation, height=300, key="pdf-animation")
    
    st.subheader("Your AI-Powered PDF Companion 📑🤖")
    st.write("""Experience the next level of PDF assistance with AI-powered search, 
    smart summarization, and instant insights from your documents.""")
    
    if user:
        st.success(f'🎉 Logged in as: {user.email}')
        col1, col2 = st.columns([1,1])
        with col1:
            if st.button("Go to Dashboard", use_container_width=True):
                st.switch_page("pages/DASHBOARD.py")
        with col2:
            if st.button("Logout", use_container_width=True):
                logout()
    
    else:
        st.info("Please log in or sign up to continue.")
        col1, col2 = st.columns([1,1])
        
        with col1:
            if st.button("Login", use_container_width=True):
                st.switch_page("pages/LOGIN.py")
        
        with col2:
            if st.button("Sign Up", use_container_width=True):
                st.switch_page("pages/SIGNUP.py")

# Show the home page
home_page()
