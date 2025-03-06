# import streamlit as st
# import os
# from db import db_manager
# from pdfminer.high_level import extract_text
# import hashlib
# import time
# import base64
# from supabase import create_client, Client

# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# st.set_page_config(page_title="📄 AI PDF Assistant", layout="wide")
# if "user" not in st.session_state:
#     session = supabase.auth.get_session()

#     if session and session.get("access_token"):
#         user = supabase.auth.get_user()
#         if user and user.get("user"):
#             st.session_state["user"] = user["user"]["id"]  # Store UUID
#             st.session_state["email"] = user["user"]["email"]
#         else:
#             st.warning("Login required.")
#             st.switch_page("pages/LOGIN.py")
#     else:
#         st.warning("Login required.")
#         st.switch_page("pages/LOGIN.py")

# # Now you can access user_id safely
# user_id = st.session_state["user"]
# st.write(f"Logged in as: {st.session_state['email']}")
# st.title("📄 AI-Powered PDF Reader & Notetaker")
# # Display the title and a logout button if user is logged in
# col1, col2 = st.columns([8, 1])  # Adjust column width for layout
# with col1:
#     st.title("📄 AI-Powered PDF Reader & Notetaker")

# with col2:
#     if "user" in st.session_state and st.session_state["user"]:
#         if st.button("🚪 Logout"):
#             st.session_state.clear()
#             st.warning("Logged out. Redirecting to login...")
#             time.sleep(2)
#             st.switch_page("pages/LOGIN.py")

# uploaded_file = st.file_uploader("📂 Upload a PDF", type=["pdf"])

# def generate_pdf_hash(pdf_file):
#     md5_hash = hashlib.md5()
#     while chunk := pdf_file.read(4096):
#         md5_hash.update(chunk)
#     pdf_file.seek(0)
#     return md5_hash.hexdigest()

# if uploaded_file:
#     pdf_hash = generate_pdf_hash(uploaded_file)
#     pdf_path = f"temp_{pdf_hash}.pdf"

#     with open(pdf_path, "wb") as f:
#         f.write(uploaded_file.getvalue())

#     existing_pdf = db_manager.get_user_pdf(user_id, pdf_hash)

#     if existing_pdf:
#         pdf_text = existing_pdf[0]
#         summary = existing_pdf[1]
#         st.write("✅ This PDF has already been processed. View the saved summary below.")
#         st.text_area("AI-Generated Summary", summary, height=150)
#     else:
#         pdf_text = extract_text(pdf_path)
#         summary = None

#     st.subheader("📜 Extracted PDF Content")
#     st.text_area("", pdf_text, height=400, label_visibility="collapsed")

#     base64_pdf = base64.b64encode(uploaded_file.read()).decode("utf-8")
#     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500px"></iframe>'
#     st.markdown(pdf_display, unsafe_allow_html=True)

#     st.subheader("💬 Chat with Your PDF")
#     user_input = st.text_input("Ask something about the PDF")

#     if st.button("Chat"):
#         if user_input:
#             response = db_manager.chat_with_gpt(user_input, pdf_text)
#             st.write(response)
#         else:
#             st.warning("Please enter a question.")

#     if not existing_pdf and st.button("📝 Generate AI Summary"):
#         summary = db_manager.generate_summary(pdf_text)
#         st.text_area("AI-Generated Summary", summary, height=150)
#         db_manager.save_user_pdf(user_id, pdf_hash, pdf_text, summary)

#     st.subheader("🗒️ Notes")
#     note_input = st.text_area("Write your notes here")

#     if st.button("Save Note"):
#         if note_input.strip():
#             db_manager.save_user_note(user_id, pdf_hash, note_input)
#             st.success("Note saved successfully!")
#         else:
#             st.warning("Note cannot be empty.")

#     if st.button("📂 Show Saved Notes"):
#         notes = db_manager.get_user_notes(user_id, pdf_hash)
#         st.text_area("Saved Notes", "\n".join(notes) if notes else "No notes found.", height=200)

#     os.remove(pdf_path)

# if st.button("Logout"):
#     supabase.auth.sign_out()
#     st.session_state.clear()
#     st.warning("Logged out, Please log back in.")
#     st.switch_page("pages/LOGIN.py")


'''
main file lower
'''
# import streamlit as st
# import os
# import time
# import logging
# from supabase import create_client, Client

# # Set up logging
# logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)

# # Initialize Supabase
# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# st.set_page_config(page_title="📄 AI PDF Assistant", layout="wide")

# logging.info("🚀 Dashboard page loaded.")

# # Ensure user session persists
# if "user" not in st.session_state:
#     logging.info("🔍 Checking existing session...")
#     session = supabase.auth.get_session()

#     if session:
#         logging.debug(f"Session data: {session}")
#         access_token = session.get("access_token")
        
#         if access_token:
#             logging.info("✅ Access token found, fetching user data...")
#             user = supabase.auth.get_user()
            
#             if user and user.get("user"):
#                 st.session_state["user"] = user["user"]["id"]
#                 st.session_state["email"] = user["user"]["email"]
#                 st.session_state["name"] = user["user"].get("user_metadata", {}).get("full_name", "User")
                
#                 logging.info(f"🎉 User authenticated: {st.session_state['email']} ({st.session_state['user']})")
#             else:
#                 logging.warning("⚠️ Failed to fetch user details, redirecting to login...")
#                 time.sleep(2)
#                 st.switch_page("pages/LOGIN.py")
#         else:
#             logging.warning("⚠️ No access token found, redirecting to login...")
#             time.sleep(2)
#             st.switch_page("pages/LOGIN.py")
#     else:
#         logging.warning("⚠️ No session found, redirecting to login...")
#         time.sleep(2)
#         st.switch_page("pages/LOGIN.py")

# # Display dashboard if user is authenticated
# if "user" in st.session_state and st.session_state["user"]:
#     st.title("📄 AI-Powered PDF Assistant")
#     st.write(f"Welcome, **{st.session_state.get('name', 'User')}** 👋")

#     logging.info("✅ User successfully loaded the dashboard.")

#     # Logout Button
#     if st.button("Logout"):
#         logging.info("🚪 User clicked logout.")
#         supabase.auth.sign_out()
#         st.session_state.clear()
#         logging.info("🔄 User session cleared, redirecting to login.")
#         st.success("Logged out. Redirecting...")
#         time.sleep(2)
#         st.switch_page("pages/LOGIN.py")

# else:
#     logging.warning("⚠️ Session not found in state, redirecting to login...")
#     time.sleep(2)
#     st.switch_page("pages/LOGIN.py")

'''
Test
'''
# import streamlit as st
# import os
# import time
# from supabase import create_client, Client
# import urllib.parse

# # Supabase credentials
# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# st.set_page_config(page_title="Dashboard", layout="wide")

# # ✅ Extract Google OAuth Code from URL
# query_params = st.query_params
# code = query_params.get("code")
# print(code)

# if code and "access_token" not in st.session_state:
#     st.success("✅ Google OAuth code received! Fetching session...")
    
#     try:
#         response = supabase.auth.exchange_code_for_session({"auth_code": code})
#         if response.user:
#             print({"user": response.user, "session": response.session})
#         session = response.session
#         print("session:",session)
#         if session:
#             st.session_state["access_token"] = session.access_token
#             st.session_state["refresh_token"] = session.refresh_token
#             st.session_state["user_email"] = session.user.email

#             st.success("✅ Google Login Successful!")
#             time.sleep(2)
#             st.rerun()  # Reload page to remove code from URL

#     except Exception as e:
#         st.error(f"❌ Failed to fetch session: {e}")

# # Check if logged in
# if "access_token" in st.session_state:
#     st.sidebar.success(f"✅ Logged in as {st.session_state['user_email']}")
#     st.write("### Welcome to your Dashboard!")
# else:
#     st.sidebar.error("❌ Please log in first.")

# # # Display welcome message and user details
# # if session:
# #     user_name=session['user']['user_metadata'].get('name')
# #     avatar_url = session['user']['user_metadata'].get('avatar_url')
# #     email_verified = session['user']['user_metadata'].get('email_verified')
# #     if not email_verified:
# #         st.error("Please use a verified email address to log in.")
# #     else:
# #         # Additional logic for when the user is authenticated...
# #         st.write(f"Welcome {user_name}!")
# #         with st.sidebar:
# #                 if user_name:  # Checking if user_name exists before attempting to display it
# #                     st.write(f"Welcome {user_name}!")
# #                 if avatar_url:  # Similarly, check for avatar_url
# #                     st.image(avatar_url, width=100)
# #                 logout_button(url=SUPABASE_URL, apiKey=SUPABASE_ANON_KEY)
# # ######</SUPABASE OAUTH>#####


import streamlit as st

def logout():
    st.session_state.user = None
    st.session_state.page = 'HOME.py'
    st.rerun()

def dashboard_page():
    try:
        if 'user' not in st.session_state:
            st.session_state.user = {}

        user = st.session_state.user
        print(user)
        
        if user or 'email' in user:
            with st.expander('User Information'):
                st.success(f'🎉 Logged in as: {user.email}')
                if hasattr(user, 'user_metadata') and "full_name" in user.user_metadata:
                    st.write(f'Username: {user.user_metadata["email"]}')
            if st.button('Logout'):
                logout()
        else:
            st.warning("Please log in to access the dashboard.")
    except Exception as e:
        st.error(f"❌ Error: {e}")
    
if __name__ == '__main__':
    dashboard_page()