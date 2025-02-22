import os
import streamlit as st
import time
from supabase import create_client, Client

# Supabase Credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Page Config
st.set_page_config(page_title="🔑 Reset Password", layout="centered")

# Custom Styling
page_styles = """
<style>
    body {
        background-color: #1a1a1a;
        color: #32a852; /* Dark Green Text */
        font-family: Arial, sans-serif;
    }
    .reset-container {
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
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 18px;
        transition: 0.3s ease;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #ff1a1a;
        transform: scale(1.05);
    }
    .back-to-login a {
        color: #32a852;
        text-decoration: none;
        font-weight: bold;
    }
    .back-to-login a:hover {
        text-decoration: underline;
    }
</style>
"""
st.markdown(page_styles, unsafe_allow_html=True)

# Reset Password Page UI
st.markdown("<h2 style='text-align: center;'>🔑 Reset Your Password</h2>", unsafe_allow_html=True)

with st.container():
    reset_email = st.text_input("Enter your email", placeholder="📩 Your registered email")

    if st.button("Send Reset Link"):
        if reset_email:
            try:
                supabase.auth.reset_password_for_email(reset_email)
                st.success(f"✅ Password reset email sent! Check your inbox.")

                # Redirect to Login Page after 3 seconds
                time.sleep(3)
                st.switch_page("login.py")

            except Exception as e:
                st.error(f"❌ Error: {e}")
        else:
            st.warning("⚠️ Please enter your email.")

# Back to Login Link
st.markdown('<div class="back-to-login"><a href="pages/login.py">← Back to Login</a></div>', unsafe_allow_html=True)
