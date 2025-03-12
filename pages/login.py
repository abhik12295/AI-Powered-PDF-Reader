# import streamlit as st
# from supabase import Client, create_client
# import os
# from dotenv import load_dotenv

# load_dotenv()
# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# def show_user_info(user):
#     with st.expander('User Information'):
#         st.success(f'🎉 Logged in as: {user.email}')
#         if hasattr(user, 'user_metadata') and "full_name" in user.user_metadata:
#             st.write(f'Username: {user.user_metadata["full_name"]}')

# def login_page():
#     st.title("Login 🔒")
    
#     email = st.text_input('Email', key='login_email')
#     password = st.text_input('Password', type='password', key='login_password')

#     if st.button("Login"):
#         try:
#             res = supabase.auth.sign_in_with_password({"email": email, "password": password})
            
#             if res.user:
#                 st.session_state.user = res.user
#                 #show_user_info(res.user)
#                 # st.session_state.page = "pages/DASHBOARD.py"
#                 # st.rerun()
#                 st.success("🎉 Login successful!")
#                 st.switch_page("pages/DASHBOARD.py")


#         except Exception as e:
#             st.warning(f"Note: You must provide an email and a password")
#             #❌
            
#     # 🔗 Forgot Password & Signup Links
#     if st.button("Forgot Password?", key="forgot_password_btn", use_container_width=True):
#         st.switch_page("pages/FORGOT PASSWORD.py")

#     st.markdown("Don't have an account?")
#     if st.button("Sign Up", key="signup_btn", use_container_width=True):
#         st.switch_page("pages/SIGNUP.py")



# if __name__ == '__main__':
#     login_page()

import streamlit as st
from supabase import Client, create_client
import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def show_user_info(user):
    with st.expander('User Information'):
        st.success(f'🎉 Logged in as: {user.email}')
        if hasattr(user, 'user_metadata') and "full_name" in user.user_metadata:
            st.write(f'Username: {user.user_metadata["full_name"]}')

def login_page():
    st.title("Login 🔒")

    # 🔹 If user is already logged in, redirect to Dashboard
    if "user" in st.session_state and st.session_state.user:
        st.success("✅ You are already logged in!")
        if st.button("Go to Dashboard"):
            st.switch_page("pages/DASHBOARD.py")
        return  # Stop further execution
    
    # 🔹 Login Form
    email = st.text_input('Email', key='login_email')
    password = st.text_input('Password', type='password', key='login_password')

    if st.button("Login"):
        try:
            res = supabase.auth.sign_in_with_password({"email": email, "password": password})
            if res.user:
                st.session_state.user = res.user
                st.success("🎉 Login successful!")
                st.switch_page("pages/DASHBOARD.py")

        except Exception as e:
            st.warning("⚠️ Invalid email or password. Please try again.")

    # 🔗 Forgot Password & Signup Links
    if st.button("Forgot Password?", key="forgot_password_btn", use_container_width=True):
        st.switch_page("pages/FORGOT PASSWORD.py")

    st.markdown("Don't have an account?")
    if st.button("Sign Up", key="signup_btn", use_container_width=True):
        st.switch_page("pages/SIGNUP.py")

if __name__ == '__main__':
    login_page()
