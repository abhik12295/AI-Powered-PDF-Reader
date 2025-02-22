import os
import json
import hashlib
import base64
import http.client
import streamlit as st
from pdfminer.high_level import extract_text
from dotenv import load_dotenv
import db_manager 

load_dotenv()
RAPIDAPI_KEY = os.getenv("rapidapi_key")

def chat_with_gpt(prompt, pdf_text):
    conn = http.client.HTTPSConnection("gpt-4o.p.rapidapi.com")
    
    payload = json.dumps({
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are an AI assistant helping with PDF analysis."},
            {"role": "user", "content": f"Here is the PDF content:\n{pdf_text}\n\nUser query: {prompt}"}
        ]
    })

    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "gpt-4o.p.rapidapi.com",
        'Content-Type': "application/json"
    }

    conn.request("POST", "/chat/completions", payload, headers)
    res = conn.getresponse()
    data = res.read()
    
    try:
        response = json.loads(data.decode("utf-8"))
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

def extract_text_from_pdf(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception as e:
        return f"Error extracting text: {e}"

def generate_pdf_hash(pdf_file):
    md5_hash = hashlib.md5()
    while chunk := pdf_file.read(4096):
        md5_hash.update(chunk)
    pdf_file.seek(0)  # Reset file pointer after hashing
    return md5_hash.hexdigest()

def generate_summary(pdf_text):
    return chat_with_gpt("Summarize this document.", pdf_text)

user_id = st.text_input("Enter User ID (For Multi-User Support)")

# Initialize database
db_manager.initialize_db()

# Streamlit UI
st.set_page_config(page_title="📄 AI PDF Assistant", layout="wide")
st.title("📄 AI-Powered PDF Reader & Notetaker")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    pdf_hash = generate_pdf_hash(uploaded_file)  # Unique ID for the file
    pdf_path = f"temp_{pdf_hash}.pdf"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    # Check if PDF has been processed before
    existing_pdf = db_manager.get_processed_pdf(pdf_hash)

    if existing_pdf:
        pdf_text = existing_pdf[0]  # Use saved text
        summary = existing_pdf[1]  # Use saved summary
        st.write("✅ This PDF has already been processed. You can view the saved summary below.")
        st.text_area("AI-Generated Summary", summary, height=150)
    else:
        pdf_text = extract_text_from_pdf(pdf_path)
        summary = None  # No summary exists yet

    col1, col2 = st.columns([2, 1])  # Main content and sidebar

    with col1:
        st.subheader("📜 Extracted PDF Content")
        st.text_area("", pdf_text, height=400, label_visibility="collapsed")

        # PDF.js Viewer
        st.subheader("📄 View PDF")
        base64_pdf = base64.b64encode(uploaded_file.read()).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500px"></iframe>'

        st.markdown(pdf_display, unsafe_allow_html=True)

        st.subheader("💬 Chat with Your PDF")
        user_input = st.text_input("Ask something about the PDF", label_visibility="collapsed")
        
        if st.button("Chat"):
            if user_input:
                response = chat_with_gpt(user_input, pdf_text)
                st.write(response)
            else:
                st.warning("Please enter a question.")

        if not existing_pdf and st.button("📝 Generate AI Summary"):
            summary = generate_summary(pdf_text)
            st.text_area("AI-Generated Summary", summary, height=150)
            # Save processed PDF to DB
            db_manager.save_processed_pdf(pdf_hash, pdf_text, summary)

    with col2:
        st.subheader("🗒️ Notes")
        note_input = st.text_area("Write your notes here", label_visibility="visible")
        
        if st.button("Save Note"):
            if note_input.strip():
                db_manager.save_note_to_db(note_input, pdf_hash)
                st.success("Note saved successfully!")
            else:
                st.warning("Note cannot be empty.")

        if st.button("📂 Show Saved Notes"):
            notes = db_manager.get_saved_notes(pdf_hash)
            st.text_area("Saved Notes", "\n".join(notes) if notes else "No notes found.", height=200, label_visibility="collapsed")

    os.remove(pdf_path)
