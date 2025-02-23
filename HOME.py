import streamlit as st
import os
import time
from supabase import Client, create_client
from dotenv import load_dotenv
from st_pages import add_page_title, get_nav_from_toml

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="🔐 Welcome!", layout="centered", 
                   initial_sidebar_state = 'collapsed',
                    )
st.title("📄 AI PDF Assistant")


if "user" not in st.session_state or not st.session_state.user:
    st.info("Please log in or sign up to continue.")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            st.switch_page("pages/LOGIN.py")
    with col2:
        if st.button("Signup"):
            st.switch_page("pages/SIGN UP.py")
else:
    st.success("✅ Redirecting to PDF Processing App...")
    st.switch_page("pages/main.py")


