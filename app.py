import streamlit as st
import os
import time
from supabase import Client, create_client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="🔐 Welcome!", layout="centered")
st.title("📄 AI PDF Assistant")

login = st.Page("pages/login.py", title= "Login")
signup = st.Page("pages/signup.py", title= "Registration")
pg = st.navigation([login, signup])

if "user" not in st.session_state or not st.session_state.user:
    st.info("Please log in or sign up to continue.")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            st.switch_page("pages/login.py")
    with col2:
        if st.button("Signup"):
            st.switch_page("pages/signup.py")
else:
    st.success("✅ Redirecting to PDF Processing App...")
    st.switch_page("pages/main.py")