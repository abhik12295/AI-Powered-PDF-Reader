# import streamlit as st
# from db.db_manager import generate_pdf_hash, get_user_pdf, get_user_pdfs, extract_text,chat_with_gpt, generate_summary,save_user_pdfs, save_user_note, get_user_note ,delete_user_pdf, rename_user_pdf
# import base64


# if 'user' not in st.session_state or st.session_state.user is None:
#     st.warning("Not logged in please go to Home for login or signup!")


# def logout():
#     st.session_state.user = None
#     st.session_state.page = 'HOME.py'
#     st.rerun()

# def dashboard_page():
#     try:
#         if 'user' not in st.session_state:
#             st.session_state.user = None

#         user = st.session_state.user
#         print(user)
#         if user or isinstance(user, dict) or 'email' in user:
#             with st.expander('User Information'):
#                 st.success(f'🎉 Logged in as: {user.email}')
#                 st.write(user.email_verified)
#                 if hasattr(user, 'user_metadata') and 'email' in user.user_metadata:
#                     st.write(f'Email final: {user.email}')
#                     st.write(f'Username: {user.user_metadata["email"]}')    
#             #clean after this
#             #if user entered then upload and gpt feature for that user


#             uploaded_file = st.file_uploader("📂 Upload a PDF", type=["pdf"])
#             search_query = st.text_input("🔍 Search saved PDFs", "")

#             print("check1")
#             # Show existing pdfs
#             user_pdfs = get_user_pdfs(user.user_metadata["id"])
#             print("user_pdfs", user_pdfs)
#             filtered_pdfs = [pdf for pdf in user_pdfs if search_query.lower() in pdf["pdf_name"].lower()]

#             if user_pdfs:
#                 st.subheader("📂 Your Saved PDFs")
#                 for pdf in filtered_pdfs:
#                     col1, col2, col3 = st.columns([4, 2, 1])

#                     with col1:
#                         new_name = st.text_input(f"Rename {pdf['pdf_name']}", pdf['pdf_name'])
                        
#                     with col2:
#                         if st.button("Rename", key=f"rename_{pdf['pdf_hash']}"):
#                             rename_user_pdf(user["id"], pdf["pdf_hash"], new_name)
#                             st.success(f"Renamed to: {new_name}")
#                             st.rerun()

#                     with col3:
#                         if st.button(f"🗑️ Delete", key=pdf["pdf_hash"]):
#                             delete_user_pdf(user["id"], pdf["pdf_hash"])
#                             st.warning(f"Deleted {pdf['pdf_name']}")
#                             st.rerun()
#             else:
#                 st.info("No PDFs saved. You can upload up to **5 PDFs**.")

#             if uploaded_file:
#                 pdf_hash = generate_pdf_hash(uploaded_file)
#                 pdf_path = f"temp_{pdf_hash}.pdf"

#                 with open(pdf_path, "wb") as f:
#                     f.write(uploaded_file.getvalue())

#                 existing_pdf = get_user_pdf(user["id"], pdf_hash)

#                 if existing_pdf:
#                     pdf_text = existing_pdf["extracted_text"] #0
#                     summary = existing_pdf["summary"] #1
#                     st.write("✅ This PDF has already been processed. View the saved summary below.")
#                     st.text_area("AI-Generated Summary", summary, height=150)
#                 else:
#                     pdf_text = extract_text(pdf_path)
#                     summary = None

#                 st.subheader("📜 Extracted PDF Content")
#                 st.text_area("", pdf_text, height=400, label_visibility="collapsed")

#                 base64_pdf = base64.b64encode(uploaded_file.read()).decode("utf-8")
#                 pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500px"></iframe>'
#                 st.markdown(pdf_display, unsafe_allow_html=True)

#                 st.subheader("💬 Chat with Your PDF")
#                 user_input = st.text_input("Ask something about the PDF")

#                 if st.button("Chat"):
#                     if user_input:
#                         response = chat_with_gpt(user_input, pdf_text)
#                         st.write(response)
#                     else:
#                         st.warning("Please enter a question.")

#                 if not existing_pdf and st.button("📝 Generate AI Summary"):
#                     summary = generate_summary(pdf_text)
#                     st.text_area("AI-Generated Summary", summary, height=150)
#                     save_user_pdfs(user, pdf_hash, pdf_text, summary)

#                 st.subheader("🗒️ Notes")
#                 note_input = st.text_area("Write your notes here")

#                 if st.button("Save Note"):
#                     if note_input.strip():
#                         save_user_note(user, pdf_hash, note_input)
#                         st.success("Note saved successfully!")
#                     else:
#                         st.warning("Note cannot be empty.")

#                 if st.button("📂 Show Saved Notes"):
#                     notes = get_user_note(user, pdf_hash)
#                     st.text_area("Saved Notes", "\n".join(notes) if notes else "No notes found.", height=200)


#             ##### clear before this
#             # if st.button('Logout'):
#             #     logout()

#         else:
#             st.warning("Please log in or got to home page to access the dashboard.")
#             if st.button("Go to Home"):
#                 st.session_state.page = "HOME.py"
#                 st.rerun()

#     except Exception as e:
#         st.error(f"Error: {str(e)}. Please login on the Home Page!")
    
#     if st.button('Logout'):
#         logout()
    
# if __name__ == '__main__':
#         dashboard_page()


import streamlit as st
from db.db_manager import (
    generate_pdf_hash, get_user_pdf, get_user_pdfs, extract_text,
    chat_with_gpt, generate_summary, save_user_pdfs, save_user_note,
    get_user_note, delete_user_pdf, rename_user_pdf
)
import base64

if 'user' not in st.session_state or st.session_state.user is None:
    st.warning("Not logged in! Please go to Home for login or signup!")


def logout():
    st.session_state.user = None
    st.session_state.page = 'HOME.py'
    st.rerun()


def dashboard_page():
    try:
        if 'user' not in st.session_state:
            st.session_state.user = None

        user = st.session_state.user
        print(user)

        # Ensure user is logged in properly
        if not user or not hasattr(user, "email"):
            st.warning("Please log in or go to the home page to access the dashboard.")
            if st.button("Go to Home"):
                st.session_state.page = "HOME.py"
                st.rerun()
            return

        # User Information Display
        with st.expander('User Information'):
            st.success(f'🎉 Logged in as: {user.email}')

            # if hasattr(user, "id"):
            #     st.write(f'User ID: {user.id}')

            if hasattr(user, "user_metadata") and isinstance(user.user_metadata, dict):
                if "email" or " email_verified" in user.user_metadata:
                    st.write(f'User Email: {user.user_metadata["email"]}')
                

        # Upload PDF Section
        uploaded_file = st.file_uploader("📂 Upload a PDF", type=["pdf"])
        search_query = st.text_input("🔍 Search saved PDFs", "")

        print("Checkpoint 1: Before fetching PDFs")
        # Ensure user_metadata and id exist before fetching PDFs
        if hasattr(user, "id"):
                user_id = user.id
        print(user_id)
        if user_id:
            user_pdfs = get_user_pdfs(user_id)
        else:
            user_pdfs = []

        print("User PDFs:", user_pdfs)
        filtered_pdfs = [pdf for pdf in user_pdfs if search_query.lower() in pdf["pdf_name"].lower()]

        # Display Saved PDFs
        if user_pdfs:
            st.subheader("📂 Your Saved PDFs")
            for pdf in filtered_pdfs:
                col1, col2, col3 = st.columns([4, 2, 1])

                with col1:
                    new_name = st.text_input(f"Rename {pdf['pdf_name']}", pdf['pdf_name'])

                with col2:
                    if st.button("Rename", key=f"rename_{pdf['pdf_hash']}"):
                        rename_user_pdf(user_id, pdf["pdf_hash"], new_name)
                        st.success(f"Renamed to: {new_name}")
                        st.rerun()

                with col3:
                    if st.button(f"🗑️ Delete", key=pdf["pdf_hash"]):
                        delete_user_pdf(user_id, pdf["pdf_hash"])
                        st.warning(f"Deleted {pdf['pdf_name']}")
                        st.rerun()
        else:
            st.info("No PDFs saved. You can upload up to **5 PDFs**.")

        # PDF Processing Section
        if uploaded_file:
            pdf_hash = generate_pdf_hash(uploaded_file)
            pdf_path = f"temp_{pdf_hash}.pdf"

            with open(pdf_path, "wb") as f:
                f.write(uploaded_file.getvalue())

            existing_pdf = get_user_pdf(user_id, pdf_hash)

            if existing_pdf:
                pdf_text = existing_pdf["extracted_text"]
                summary = existing_pdf["summary"]
                st.write("✅ This PDF has already been processed. View the saved summary below.")
                st.text_area("AI-Generated Summary", summary, height=150)
            else:
                pdf_text = extract_text(pdf_path)
                summary = None

            st.subheader("📜 Extracted PDF Content")
            st.text_area("", pdf_text, height=400, label_visibility="collapsed")

            base64_pdf = base64.b64encode(uploaded_file.read()).decode("utf-8")
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500px"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

            # Chat with PDF
            st.subheader("💬 Chat with Your PDF")
            user_input = st.text_input("Ask something about the PDF")

            if st.button("Chat"):
                if user_input:
                    response = chat_with_gpt(user_input, pdf_text)
                    st.write(response)
                else:
                    st.warning("Please enter a question.")

            if not existing_pdf and st.button("📝 Generate AI Summary"):
                summary = generate_summary(pdf_text)
                st.text_area("AI-Generated Summary", summary, height=150)
                save_user_pdfs(user, pdf_hash, pdf_text, summary)

            # Notes Section
            st.subheader("🗒️ Notes")
            note_input = st.text_area("Write your notes here")

            if st.button("Save Note"):
                if note_input.strip():
                    save_user_note(user, pdf_hash, note_input)
                    st.success("Note saved successfully!")
                else:
                    st.warning("Note cannot be empty.")

            if st.button("📂 Show Saved Notes"):
                notes = get_user_note(user, pdf_hash)
                st.text_area("Saved Notes", "\n".join(notes) if notes else "No notes found.", height=200)

        if st.button("Logout"):
            logout()

    except Exception as e:
        st.error(f"Error: {str(e)}. Please login on the Home Page!")
        if st.button("Go to Home"):
            st.session_state.page = "HOME.py"
            st.rerun()


if __name__ == '__main__':
    dashboard_page()
