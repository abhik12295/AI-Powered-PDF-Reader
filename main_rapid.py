import os
import http.client
import json
import streamlit as st
import fitz
from dotenv import load_dotenv
import sqlite3

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

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    """Extracts text from an uploaded PDF file."""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "\n".join([page.get_text("text") for page in doc])
    return text

# Function to save notes in SQLite
def save_note_to_db(note):
    """Saves user notes to a SQLite database."""
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, note TEXT)")
    c.execute("INSERT INTO notes (note) VALUES (?)", (note,))
    conn.commit()
    conn.close()

# Function to retrieve saved notes
def get_saved_notes():
    """Fetches saved notes from the database."""
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("SELECT note FROM notes")
    notes = [row[0] for row in c.fetchall()]
    conn.close()
    return notes

# Function to generate AI summary of the PDF
def generate_summary(pdf_text):
    """Generates an AI-powered summary of the PDF content."""
    return chat_with_gpt("Summarize this document.", pdf_text)

# Streamlit UI Configuration
st.set_page_config(page_title="📄 AI PDF Assistant", layout="wide")
st.title("📄 AI-Powered PDF Reader & Notetaker")

# File Uploader
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    pdf_text = extract_text_from_pdf(uploaded_file)

    col1, col2 = st.columns([2, 1])  # Main content and sidebar
    
    with col1:
        st.subheader("📜 Extracted PDF Content")
        st.text_area("", pdf_text, height=400, label_visibility="collapsed")

        st.subheader("💬 Chat with Your PDF")
        user_input = st.text_input("Ask something about the PDF", label_visibility="collapsed")
        
        if st.button("Chat"):
            if user_input:
                response = chat_with_gpt(user_input, pdf_text)
                st.write(response)
            else:
                st.warning("Please enter a question.")

        if st.button("📝 Generate AI Summary"):
            summary = generate_summary(pdf_text)
            st.text_area("AI-Generated Summary", summary, height=150, label_visibility="collapsed")

    with col2:
        st.subheader("🗒️ Notes")
        note_input = st.text_area("Write your notes here", label_visibility="visible")
        
        if st.button("Save Note"):
            if note_input.strip():
                save_note_to_db(note_input)
                st.success("Note saved successfully!")
            else:
                st.warning("Note cannot be empty.")

        if st.button("📂 Show Saved Notes"):
            notes = get_saved_notes()
            st.text_area("Saved Notes", "\n".join(notes) if notes else "No notes found.", height=200, label_visibility="collapsed")
