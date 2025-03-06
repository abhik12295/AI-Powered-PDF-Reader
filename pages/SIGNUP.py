# import os
# import time
# import streamlit as st
# from supabase import create_client, Client

# # Supabase Credentials
# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# # Page Configuration
# st.set_page_config(page_title="Register to AI PDF Assistant", layout="centered", initial_sidebar_state = 'collapsed')


# # Custom Styling
# page_styles = """
# <style>
#     body {
#         background-color: #1a1a1a;
#         color: #32a852;
#         font-family: Arial, sans-serif;
#     }
#     .signup-container {
#         width: 400px;
#         margin: auto;
#         padding: 30px;
#         background: rgba(255, 255, 255, 0.1);
#         border-radius: 15px;
#         box-shadow: 0px 4px 12px rgba(50, 168, 82, 0.5);
#         text-align: center;
#     }
#     .stTextInput > div > div > input {
#         border-radius: 10px;
#         padding: 12px;
#         font-size: 16px;
#         border: 1px solid #32a852;
#         background-color: #333;
#         color: white;
#     }
#     .stTextInput > div > div > input::placeholder {
#         color: #bbb;
#     }
#     .stButton > button {
#         background-color: #32a852;
#         color: white;
#         border-radius: 10px;
#         padding: 10px 20px;
#         font-size: 18px;
#         transition: 0.3s ease;
#         width: 100%;
#     }
#     .stButton > button:hover {
#         background-color: #28a745;
#         transform: scale(1.05);
#     }
#     .google-btn img {
#         width: 100%;
#         height: 48px;
#         cursor: pointer;
#         border-radius: 10px;
#     }
#     .login-link {
#         margin-top: 15px;
#         text-align: center;
#     }
#     .login-link a {
#         color: #32a852;
#         text-decoration: none;
#         font-weight: bold;
#     }
#     .login-link a:hover {
#         text-decoration: underline;
#     }
# </style>
# """
# st.markdown(page_styles, unsafe_allow_html=True)

# with st.container():
#     email = st.text_input("Email", placeholder="📧 Enter your email")
#     password = st.text_input("Password", type= "password",placeholder="🔑 Create a password")
#     confirm_password = st.text_input("Confirm Password", type="password", placeholder="🔑 Confirm your password")

#     if password and confirm_password and password != confirm_password:
#         st.error("❌ Passwords do not match!")
    
#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button("Sign Up"):
#             if password == confirm_password:
#                 try:
#                     response = supabase.auth.sign_up({"email":email, "password": password})
#                     if response.user:
#                         st.success("✅ Account created successfully! Please check your email to verify.")
#                         time.sleep(2)
#                         st.switch_page("LOGIN.py")
#                 except Exception as e:
#                     st.error(f"❌ Error: {e}")
#             else:
#                 st.error("❌ Passwords must match!")

#     with col2:
#         google_auth_url = supabase.auth.sign_in_with_oauth({"provider": "google"}).url
#         google_logo_path = "https://developers.google.com/static/identity/images/btn_google_signin_dark_normal_web.png"
#         st.markdown(f'<a href="{google_auth_url}" class="google-btn"><img src="{google_logo_path}" alt="Google Sign-Up"></a>', unsafe_allow_html=True)
    
#     st.markdown("Already have an account?") 
#     if st.button("Login"):
#         st.switch_page("pages/LOGIN.py")
import streamlit as st
from supabase import Client
from supabase import create_client
import os

#Initialize Supabase client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase:Client = create_client(SUPABASE_URL, SUPABASE_KEY)

import streamlit as st
from supabase import Client, create_client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def signup_page():
    st.title("Sign Up 📝")
    new_email = st.text_input('Email', key='signup_email')
    new_password = st.text_input('Password', type='password', key='signup_password')
    
    if st.button("Sign Up"):
        res = supabase.auth.sign_up({"email": new_email, "password": new_password})
        
        if res.user:
            st.success("🎉 Signup successful!")
            st.session_state.page = "login"
        else:
            st.warning("Signup failed. Please try again.")

if __name__ == '__main__':
    signup_page()