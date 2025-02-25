import streamlit as st
import os
from db import db_manager
from pdfminer.high_level import extract_text
import hashlib
import time
import base64

st.set_page_config(page_title="📄 AI PDF Assistant", layout="wide")

if "user" not in st.session_state:
    st.warning("Please log in first.")
    time.sleep(3)  # Pause for 5 seconds
    st.switch_page("pages/LOGIN.py")

user_id = st.session_state["user"]

st.title("📄 AI-Powered PDF Reader & Notetaker")

uploaded_file = st.file_uploader("📂 Upload a PDF", type=["pdf"])

def generate_pdf_hash(pdf_file):
    md5_hash = hashlib.md5()
    while chunk := pdf_file.read(4096):
        md5_hash.update(chunk)
    pdf_file.seek(0)
    return md5_hash.hexdigest()

if uploaded_file:
    pdf_hash = generate_pdf_hash(uploaded_file)
    pdf_path = f"temp_{pdf_hash}.pdf"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    existing_pdf = db_manager.get_user_pdf(user_id, pdf_hash)

    if existing_pdf:
        pdf_text = existing_pdf[0]
        summary = existing_pdf[1]
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

    st.subheader("💬 Chat with Your PDF")
    user_input = st.text_input("Ask something about the PDF")

    if st.button("Chat"):
        if user_input:
            response = db_manager.chat_with_gpt(user_input, pdf_text)
            st.write(response)
        else:
            st.warning("Please enter a question.")

    if not existing_pdf and st.button("📝 Generate AI Summary"):
        summary = db_manager.generate_summary(pdf_text)
        st.text_area("AI-Generated Summary", summary, height=150)
        db_manager.save_user_pdf(user_id, pdf_hash, pdf_text, summary)

    st.subheader("🗒️ Notes")
    note_input = st.text_area("Write your notes here")

    if st.button("Save Note"):
        if note_input.strip():
            db_manager.save_user_note(user_id, pdf_hash, note_input)
            st.success("Note saved successfully!")
        else:
            st.warning("Note cannot be empty.")

    if st.button("📂 Show Saved Notes"):
        notes = db_manager.get_user_notes(user_id, pdf_hash)
        st.text_area("Saved Notes", "\n".join(notes) if notes else "No notes found.", height=200)

    os.remove(pdf_path)

if st.button("Logout"):
    st.session_state.clear()
    st.warning("Logged out, Please log back in.")
    st.switch_page("pages/Login.py")
