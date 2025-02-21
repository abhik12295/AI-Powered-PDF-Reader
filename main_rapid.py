import os
import json
import http.client
import hashlib
import sqlite3
import streamlit as st
from pdfminer.high_level import extract_text
from dotenv import load_dotenv
import base64


# Load environment variables
load_dotenv()
RAPIDAPI_KEY = os.getenv("rapidapi_key")

# Function to connect to GPT-4o via RapidAPI
def chat_with_gpt(prompt, pdf_text):
    """Sends user query along with PDF content to GPT-4o via RapidAPI."""
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

# Function to extract text from PDF using pdfminer
def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file using pdfminer.six."""
    try:
        return extract_text(pdf_path)
    except Exception as e:
        return f"Error extracting text: {e}"

# Function to generate a hash for PDF files
def generate_pdf_hash(pdf_file):
    """Generate a hash to identify unique PDFs."""
    md5_hash = hashlib.md5()
    while chunk := pdf_file.read(4096):
        md5_hash.update(chunk)
    pdf_file.seek(0)  # Reset file pointer after hashing
    return md5_hash.hexdigest()

# Function to save notes in SQLite
def save_note_to_db(note, pdf_hash):
    """Saves user notes linked to a specific PDF."""
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, pdf_hash TEXT, note TEXT)")
    c.execute("INSERT INTO notes (pdf_hash, note) VALUES (?, ?)", (pdf_hash, note))
    conn.commit()
    conn.close()

# Function to get saved notes for a PDF
def get_saved_notes(pdf_hash):
    """Retrieves notes linked to a specific PDF."""
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("SELECT note FROM notes WHERE pdf_hash=?", (pdf_hash,))
    notes = [row[0] for row in c.fetchall()]
    conn.close()
    return notes

# Function to generate an AI summary of the PDF
def generate_summary(pdf_text):
    """Generates an AI-powered summary of the PDF content."""
    return chat_with_gpt("Summarize this document.", pdf_text)

# Streamlit UI
st.set_page_config(page_title="📄 AI PDF Assistant", layout="wide")
st.title("📄 AI-Powered PDF Reader & Notetaker")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    pdf_hash = generate_pdf_hash(uploaded_file)  # Unique ID for the file
    pdf_path = f"temp_{pdf_hash}.pdf"

    # Save uploaded PDF temporarily
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    # Extract text from PDF using pdfminer.six
    pdf_text = extract_text_from_pdf(pdf_path)

    # Connect to DB & check if this PDF has been processed before
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS processed_pdfs (hash TEXT PRIMARY KEY, text TEXT, summary TEXT)")
    c.execute("SELECT text, summary FROM processed_pdfs WHERE hash=?", (pdf_hash,))
    existing_pdf = c.fetchone()

    if existing_pdf:
        pdf_text = existing_pdf[0]  # Use saved text
        summary = existing_pdf[1]  # Use saved summary
        st.write("✅ This PDF has already been processed. You can view the saved summary below.")
        st.text_area("AI-Generated Summary", summary, height=150)
    else:
        summary = None  # No summary exists yet

    col1, col2 = st.columns([2, 1])  # Main content and sidebar

    with col1:
        st.subheader("📜 Extracted PDF Content")
        st.text_area("", pdf_text, height=400, label_visibility="collapsed")

        # PDF.js Viewer
        st.subheader("📄 View PDF")
        pdf_display = f"""
        <iframe src="https://mozilla.github.io/pdf.js/web/viewer.html?file={pdf_path}" width="100%" height="600px"></iframe>
        """
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
            c.execute("INSERT INTO processed_pdfs (hash, text, summary) VALUES (?, ?, ?)",
                      (pdf_hash, pdf_text, summary))
            conn.commit()

    with col2:
        st.subheader("🗒️ Notes")
        note_input = st.text_area("Write your notes here", label_visibility="visible")
        
        if st.button("Save Note"):
            if note_input.strip():
                save_note_to_db(note_input, pdf_hash)
                st.success("Note saved successfully!")
            else:
                st.warning("Note cannot be empty.")

        if st.button("📂 Show Saved Notes"):
            notes = get_saved_notes(pdf_hash)
            st.text_area("Saved Notes", "\n".join(notes) if notes else "No notes found.", height=200, label_visibility="collapsed")

    conn.close()  # Close DB connection

    # Clean up temp file
    os.remove(pdf_path)
