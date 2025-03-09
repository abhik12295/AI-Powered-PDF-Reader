# import os
# import time
# import streamlit as st
# from supabase import create_client, Client

# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# st.set_page_config(page_title="Login to AI PDF Assistant", layout="centered", initial_sidebar_state = 'collapsed')

# page_styles = """
# <style>
#     body {
#         background-color: #1a1a1a;
#         color: #32a852; /* Dark Green Text */
#         font-family: Arial, sans-serif;
#     }
#     .login-container {
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
#         background-color: #ff4b4b;
#         color: white;
#         border-radius: 10px;
#         padding: 10px 20px;
#         font-size: 18px;
#         transition: 0.3s ease;
#         width: 100%;
#     }
#     .stButton > button:hover {
#         background-color: #ff1a1a;
#         transform: scale(1.05);
#     }
#     .google-btn img {
#         width: 100%;
#         height: 48px;
#         cursor: pointer;
#         border-radius: 10px;
#     }
#     .forgot-password, .signup {
#         margin-top: 15px;
#     }
#     .forgot-password a, .signup a {
#         color: #32a852;
#         text-decoration: none;
#         font-weight: bold;
#     }
#     .forgot-password a:hover, .signup a:hover {
#         text-decoration: underline;
#     }
# </style>
# """
# st.markdown(page_styles, unsafe_allow_html=True)

# if "user" in st.session_state and st.session_state.get("user"):
#     st.switch_page("pages/DASHBOARD.py") # redirect to dashboard if session exists

# # SESSION_TIMEOUT = 1800
# # if "user" in st.session_state and time.time() - st.session_state["last_active"] > SESSION_TIMEOUT:
# #     st.session_state["user"] = None
# #     st.warning("Session expired! Please log in again.")
# #     st.switch_page("pages/LOGIN.py")

# st.markdown("<h2 style='text-align: center;'>AI PDF Assistant Login</h2>", unsafe_allow_html=True)

# with st.container():
#     email = st.text_input("Email", placeholder="📧 Enter your email")
#     password = st.text_input("Password", type="password", placeholder="🔑 Enter your password")

#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button("Login"):
#             try:
#                 response = supabase.auth.sign_in_with_password({"email": email, "password": password})
#                 if response.user:
#                     st.success("✅ Login Successful!")
#                     st.session_state["user"] = response.user.id
#                     st.session_state["email"] = email
#                     st.switch_page("pages/DASHBOARD.py")
#             except Exception as e:
#                 st.error(f"❌ Error: {e}")

#     with col2:
#         google_auth_url = supabase.auth.sign_in_with_oauth({"provider": "google"}).url
#         google_logo_path = "https://developers.google.com/static/identity/images/btn_google_signin_dark_normal_web.png"
#         st.markdown(f'<a href="{google_auth_url}" class="google-btn"><img src="{google_logo_path}" alt="Google Sign-In"></a>', unsafe_allow_html=True)

#     if "oauth_redirect" in st.session_state:
#         del st.session_state["oauth_redirect"]
#         st.switch_page("pages/DASHBOARD.py")

# if st.button("Forgot Password?", key="forgot_password_btn", use_container_width=True):
#     st.switch_page("pages/FORGOT PASSWORD.py")

# st.markdown("Don't have an account?")
# if st.button("Sign Up", key="signup_btn", use_container_width=True):
#     st.switch_page("pages/SIGN UP.py")

'''
main
'''
# import streamlit as st
# import os
# import time
# from supabase import create_client, Client

# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# st.set_page_config(page_title="Login to AI PDF Assistant", layout="centered", initial_sidebar_state='collapsed')

# page_styles = """
# <style>
#     body {
#         background-color: #1a1a1a;
#         color: #32a852; /* Dark Green Text */
#         font-family: Arial, sans-serif;
#     }
#     .login-container {
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
#         background-color: #ff4b4b;
#         color: white;
#         border-radius: 10px;
#         padding: 10px 20px;
#         font-size: 18px;
#         transition: 0.3s ease;
#         width: 100%;
#     }
#     .stButton > button:hover {
#         background-color: #ff1a1a;
#         transform: scale(1.05);
#     }
#     .google-btn img {
#         width: 100%;
#         height: 48px;
#         cursor: pointer;
#         border-radius: 10px;
#     }
#     .forgot-password, .signup {
#         margin-top: 15px;
#     }
#     .forgot-password a, .signup a {
#         color: #32a852;
#         text-decoration: none;
#         font-weight: bold;
#     }
#     .forgot-password a:hover, .signup a:hover {
#         text-decoration: underline;
#     }
# </style>
# """
# st.markdown(page_styles, unsafe_allow_html=True)

# # Check if user is already logged in
# if "access_token" in st.session_state:
#     st.session_state["user"] = supabase.auth.get_user()
#     st.session_state["email"] = st.session_state["user"]["email"]
#     st.switch_page("pages/DASHBOARD.py")

# # UI for login page
# st.markdown("<h2 style='text-align: center;'>AI PDF Assistant Login</h2>", unsafe_allow_html=True)

# with st.container():
#     email = st.text_input("Email", placeholder="📧 Enter your email")
#     password = st.text_input("Password", type="password", placeholder="🔑 Enter your password")

#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button("Login"):
#             try:
#                 response = supabase.auth.sign_in_with_password({"email": email, "password": password})
#                 if response.user:
#                     st.success("✅ Login Successful!")
#                     st.session_state["user"] = response.user.id
#                     st.session_state["email"] = email
#                     time.sleep(2)
#                     st.session_state["access_token"] = response.access_token  # Store the access token
#                     st.switch_page("pages/DASHBOARD.py")
#             except Exception as e:
#                 st.error(f"❌ Error: {e}")

#     with col2:
#         google_auth_url = supabase.auth.sign_in_with_oauth({"provider": "google"}).url
#         google_logo_path = "https://developers.google.com/static/identity/images/btn_google_signin_dark_normal_web.png"
#         st.markdown(f'<a href="{google_auth_url}" class="google-btn"><img src="{google_logo_path}" alt="Google Sign-In"></a>', unsafe_allow_html=True)

#     if "oauth_redirect" in st.session_state:
#         del st.session_state["oauth_redirect"]
#         time.sleep(2)
#         st.session_state["access_token"] = supabase.auth.get_session().get("access_token")  # Ensure access token is set
#         st.switch_page("pages/DASHBOARD.py")

# if st.button("Forgot Password?", key="forgot_password_btn", use_container_width=True):
#     st.switch_page("pages/FORGOT PASSWORD.py")

# st.markdown("Don't have an account?")
# if st.button("Sign Up", key="signup_btn", use_container_width=True):
#     st.switch_page("pages/SIGN UP.py")


# import streamlit as st
# import os
# import time
# from supabase import create_client, Client

# # Initialize Supabase
# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# st.set_page_config(page_title="Login to AI PDF Assistant", layout="centered", initial_sidebar_state='collapsed')

# # Custom Page Styles
# page_styles = """
# <style>
#     body {
#         background-color: #1a1a1a;
#         color: #32a852;
#         font-family: Arial, sans-serif;
#     }
#     .login-container {
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
#         background-color: #ff4b4b;
#         color: white;
#         border-radius: 10px;
#         padding: 10px 20px;
#         font-size: 18px;
#         transition: 0.3s ease;
#         width: 100%;
#     }
#     .stButton > button:hover {
#         background-color: #ff1a1a;
#         transform: scale(1.05);
#     }
#     .google-btn img {
#         width: 100%;
#         height: 48px;
#         cursor: pointer;
#         border-radius: 10px;
#     }
#     .forgot-password, .signup {
#         margin-top: 15px;
#     }
#     .forgot-password a, .signup a {
#         color: #32a852;
#         text-decoration: none;
#         font-weight: bold;
#     }
#     .forgot-password a:hover, .signup a:hover {
#         text-decoration: underline;
#     }
# </style>
# """
# st.markdown(page_styles, unsafe_allow_html=True)

# # 🔍 Check if user is already logged in
# if "access_token" in st.session_state:
#     st.session_state["user"] = supabase.auth.get_user()
#     st.session_state["email"] = st.session_state["user"]["email"]
#     st.switch_page("pages/DASHBOARD.py")

# # 🖥️ UI for Login Page
# st.markdown("<h2 style='text-align: center;'>AI PDF Assistant Login</h2>", unsafe_allow_html=True)

# with st.container():
#     email = st.text_input("Email", placeholder="📧 Enter your email")
#     password = st.text_input("Password", type="password", placeholder="🔑 Enter your password")

#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button("Login"):
#             try:
#                 response = supabase.auth.sign_in_with_password({"email": email, "password": password})
#                 if response.user:
#                     st.success("✅ Login Successful! Redirecting...")
#                     st.session_state["user"] = response.user
#                     st.session_state["email"] = email
#                     st.session_state["access_token"] = response.session.access_token  # Store the access token
#                     time.sleep(2)
#                     st.switch_page("pages/DASHBOARD.py")
#             except Exception as e:
#                 st.error(f"❌ Error: {e}")

#     with col2:
#         google_auth_url = supabase.auth.sign_in_with_oauth({"provider": "google"}).url
#         google_logo_path = "https://developers.google.com/static/identity/images/btn_google_signin_dark_normal_web.png"
#         st.markdown(f'<a href="{google_auth_url}" class="google-btn"><img src="{google_logo_path}" alt="Google Sign-In"></a>', unsafe_allow_html=True)

# # ✅ Handle OAuth Redirect and Store Session
# if "oauth_redirect" in st.session_state:
#     del st.session_state["oauth_redirect"]
#     time.sleep(2)  # Allow Supabase to process the OAuth login

#     session = supabase.auth.get_session()  # Retrieve session after redirect
#     if session:
#         st.session_state["access_token"] = session.access_token
#         st.session_state["user"] = session.user
#         time.sleep(2)
#         st.success("✅ Google Login Successful! Redirecting...")
#         time.sleep(2)
#         st.switch_page("pages/DASHBOARD.py")
#     else:
#         st.error("❌ OAuth Login Failed! Please try again.")

# # 🔗 Forgot Password & Signup Links
# if st.button("Forgot Password?", key="forgot_password_btn", use_container_width=True):
#     st.switch_page("pages/FORGOT PASSWORD.py")

# st.markdown("Don't have an account?")
# if st.button("Sign Up", key="signup_btn", use_container_width=True):
#     st.switch_page("pages/SIGN UP.py")

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
    
    email = st.text_input('Email', key='login_email')
    password = st.text_input('Password', type='password', key='login_password')

    if st.button("Login"):
        try:
            #st.write(f"Attempting to login with Email: {email} and Password: {password}")
            res = supabase.auth.sign_in_with_password({"email": email, "password": password})


            if res.user:
                st.session_state.user = res.user
                #show_user_info(res.user)
                st.session_state.page = "DASHBOARD.py"
                st.rerun()

                #st.switch_page("pages/DASHBOARD.py")
                st.success("🎉 Login successful!")
        except Exception as e:
            st.error(f"❌ Error: You must provide either an email and a password")

    # 🔗 Forgot Password & Signup Links
    if st.button("Forgot Password?", key="forgot_password_btn", use_container_width=True):
        st.switch_page("pages/FORGOT PASSWORD.py")

    st.markdown("Don't have an account?")
    if st.button("Sign Up", key="signup_btn", use_container_width=True):
        st.switch_page("pages/SIGNUP.py")



if __name__ == '__main__':
    login_page()