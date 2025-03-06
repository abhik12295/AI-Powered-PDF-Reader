import streamlit as st
import streamlit.components.v1 as components
import os
from supabase import Client, create_client
import requests
import subprocess
import platform
import distro
import uuid
from datetime import datetime

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def show_user_info(user):
    with st.expander('User Information'):
        st.success(f'🎉 Logged in as: {user.email}')
        if hasattr(user, 'user_metadata') and "full_name" in user.user_metadata:
            st.write(f'Username: {user.user_metadata["full_name"]}')

def show_login_signup_forms():
    col1, col2 = st.columns(2)
    with col1:
        with st.expander('Login 🔒'):
            email = st.text_input('Email', key='login_email')
            password = st.text_input('Password', type='password', key='login_password')
            login_btn = st.button('Login', on_click=login, args=(email, password))

    with col2:
        with st.expander('Sign Up 📝'):
            new_email = st.text_input('Email', key = 'signup_email')
            new_password = st.text_input('Password', type='password',key='signup_password')
            signup_btn = st.button('Sign Up', on_click=signup, args=(new_email, new_password))

def upload_file():
    file = st.file_uploader('Choose a file')
    if file is not None:
        destination = file.name
        with open(destination, 'wb') as f:
            f.write(file.read())
        
        res = supabase.storage.from_('streamlit-supabase').upload(destination, destination)
        st.success('🚀 File uploaded successfully!')

def streamlit_supabase_session():
    new_id = str(uuid.uuid4())
    time_now = datetime.now().isoformat()
    user = supabase.auth.get_user()
    if user:
        response = supabase.table("streamlit_supabase_session").insert([
            {"id":new_id,
             "created_at":time_now
             }]).execute()

def login(email, password):
    res = supabase.auth.sign_in_with_password({"email":email, "password":password})

    if res.user:
        st.session_state.user = res.user
        show_user_info(res.user)
        st.success("🎉 Login successful!")
    else:
        st.warning("Login failed. Please check your credentials.")


def signup(email, password):
    res = supabase.auth.sign_up({"email":email,"password":password})
    if res.user:
        st.success(("🎉 Signup successful!"))
    else:
        st.warning("Signup failed. Please try again.")

st.set_page_config(page_title="Home")

def main():

    streamlit_supabase_session()

    if 'user' not in st.session_state:
        st.session_state.user = {}

    #check if the user is authenticated
    user = st.session_state.user
    if user and 'email' in user:
        show_user_info(user)
    else:
        show_login_signup_forms()
    
    st.header('file upload')
    upload_file()

if __name__ == '__main__':
    main()