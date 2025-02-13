import os
import streamlit as st
import fitz
import openai
from dotenv import load_dotenv
import sqlite3

load_dotenv()
openai.api_key = os.getenv("openai_key")

def extract_text_from_pdf(pdf_file):
    """Extract text from the uploaded PDF."""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "\n".join([page.get_text("text") for page in doc])
    return text

def chat_with_pdf(prompt, pdf_text):
    """Send user prompt and PDF context to OpenAI for chat-based responses."""
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an AI assistant helping with PDF analysis."},
            {"role": "user", "content": f"Here is the PDF content:\n{pdf_text}\n\nUser query: {prompt}"}
        ]
    ).choices[0].message.content
    return response

def save_note_to_db(note):
    """Save user notes to SQLite database."""
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, note TEXT)")
    c.execute("INSERT INTO notes (note) VALUES (?)", (note,))
    conn.commit()
    conn.close()

def get_saved_notes():
    """Retrieve saved notes."""
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("SELECT note FROM notes")
    notes = [row[0] for row in c.fetchall()]
    conn.close()
    return notes

def generate_summary(pdf_text):
    """Generate AI-powered summary of the PDF."""
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Summarize the following PDF content succinctly."},
            {"role": "user", "content": pdf_text}
        ]
    ).choices[0].message.content
    return response

# Streamlit UI
st.set_page_config(page_title="AI PDF Assistant", layout="wide")
st.title("📄 AI-Powered PDF Reader & Notetaker")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    pdf_text = extract_text_from_pdf(uploaded_file)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Extracted PDF Content")
        st.text_area("", pdf_text, height=400)
        
        st.subheader("Chat with your PDF")
        user_input = st.text_input("Ask something about the PDF")
        if st.button("Chat") and user_input:
            response = chat_with_pdf(user_input, pdf_text)
            st.write(response)
        
        if st.button("Generate AI Summary"):
            summary = generate_summary(pdf_text)
            st.text_area("AI-Generated Summary", summary, height=150)
    
    with col2:
        st.subheader("Notes")
        note_input = st.text_area("Write your own notes")
        if st.button("Save Note") and note_input:
            save_note_to_db(note_input)
            st.success("Note saved successfully!")
        
        if st.button("Show Saved Notes"):
            notes = get_saved_notes()
            st.text_area("Saved Notes", "\n".join(notes) if notes else "No notes found.", height=200)
