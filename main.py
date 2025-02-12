import os
import streamlit as st
import fitz
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("openai_key")

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream = pdf_file.read(), filetype = "pdf")
    text = "\n".join([page.get_text("text") for page in doc])
    return text


st.title("AI-Powered PDF Reader & Notetaker")
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    pdf_text = extract_text_from_pdf(uploaded_file)
