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
import os
import time
from supabase import create_client, Client

# Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="Login", layout="centered")

st.markdown("<h2 style='text-align: center;'>Login to AI PDF Assistant</h2>", unsafe_allow_html=True)

# ✅ **Get OAuth Code from URL**
query_params = st.query_params
code = query_params.get("code")  # Google OAuth returns `code` in URL

if code:
    st.success("✅ Google OAuth code received! Fetching session...")
    
    # **Exchange code for session**
    try:
        response = supabase.auth.exchange_code_for_session({"code": code})
        session = response.session
        
        if session:
            st.session_state["access_token"] = session.access_token
            st.session_state["refresh_token"] = session.refresh_token
            st.session_state["user_email"] = session.user.email
            
            st.success("✅ Google Login Successful! Redirecting...")
            
            # **Log access token**
            st.text(f"Access Token: {session.access_token}")  # ✅ LOGGING ACCESS TOKEN
            print(f"Access Token: {session.access_token}")  # Log in terminal
            
            time.sleep(2)
            st.switch_page("pages/DASHBOARD.py")  # Redirect after login
            
    except Exception as e:
        st.error(f"❌ Failed to fetch session: {e}")

# Login form
email = st.text_input("Email", placeholder="📧 Enter your email")
password = st.text_input("Password", type="password", placeholder="🔑 Enter your password")

col1, col2 = st.columns(2)

# **Email & Password Login**
with col1:
    if st.button("Login"):
        try:
            response = supabase.auth.sign_in_with_password({"email": email, "password": password})
            if response.session:
                st.session_state["access_token"] = response.session.access_token
                st.session_state["refresh_token"] = response.session.refresh_token
                st.session_state["user_email"] = email
                st.success("✅ Login Successful! Redirecting...")
                time.sleep(2)
                st.switch_page("pages/DASHBOARD.py")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# **Google OAuth Login**
with col2:
    import secrets
    import base64, hashlib

    def generate_pkce_verifier():
        code_verifier = secrets.token_urlsafe(64)
        code_challenge = base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode()).digest()).decode().rstrip("=")
        return code_verifier, code_challenge
    
    if st.button("Sign in with Google"):
        code_verifier, code_challenge = generate_pkce_verifier()
        st.session_state["code_verifier"] = code_verifier 
        google_auth_url = supabase.auth.sign_in_with_oauth({
            "provider": "google",
            "redirect_to": f"http://localhost:8501/DASHBOARD",
            "scopes": "email profile",
            "code_challenge": code_challenge,
            "code_challenge_method": "S256"
            }).url
        st.session_state["oauth_redirect"] = True  # Store redirect flag in session state
        st.markdown(f'<a href="{google_auth_url}" target="_self">🔗 Click here to sign in with Google</a>', unsafe_allow_html=True)

# # **Handle OAuth Redirect (Get Session)**
# if "oauth_redirect" in st.session_state:
#     time.sleep(2)  # Give time for OAuth login
#     session = supabase.auth.get_session()  # Get the session after OAuth redirect

#     if session:
#         st.session_state["access_token"] = session.access_token
#         st.session_state["refresh_token"] = session.refresh_token
#         st.session_state["user_email"] = session.user.email
#         del st.session_state["oauth_redirect"]  # Remove redirect flag
#         st.success("✅ Google Login Successful! Redirecting...")
#         time.sleep(2)
#         st.switch_page("pages/DASHBOARD.py")
