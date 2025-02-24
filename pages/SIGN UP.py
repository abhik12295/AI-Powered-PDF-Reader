import os
import time
import streamlit as st
from supabase import create_client, Client

# Supabase Credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Page Configuration
st.set_page_config(page_title="Register to AI PDF Assistant", layout="centered", initial_sidebar_state = 'collapsed')


# Custom Styling
page_styles = """
<style>
    body {
        background-color: #1a1a1a;
        color: #32a852;
        font-family: Arial, sans-serif;
    }
    .signup-container {
        width: 400px;
        margin: auto;
        padding: 30px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(50, 168, 82, 0.5);
        text-align: center;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        border: 1px solid #32a852;
        background-color: #333;
        color: white;
    }
    .stTextInput > div > div > input::placeholder {
        color: #bbb;
    }
    .stButton > button {
        background-color: #32a852;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 18px;
        transition: 0.3s ease;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #28a745;
        transform: scale(1.05);
    }
    .google-btn img {
        width: 100%;
        height: 48px;
        cursor: pointer;
        border-radius: 10px;
    }
    .login-link {
        margin-top: 15px;
        text-align: center;
    }
    .login-link a {
        color: #32a852;
        text-decoration: none;
        font-weight: bold;
    }
    .login-link a:hover {
        text-decoration: underline;
    }
</style>
"""
st.markdown(page_styles, unsafe_allow_html=True)

with st.container():
    email = st.text_input("Email", placeholder="📧 Enter your email")
    password = st.text_input("Password", type= "password",placeholder="🔑 Create a password")
    confirm_password = st.text_input("Confirm Password", type="password", placeholder="🔑 Confirm your password")