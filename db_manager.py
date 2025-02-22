# import sqlite3

# DB_NAME = "notes.db"

# def initialize_db():
#     conn = sqlite3.connect(DB_NAME)
#     c = conn.cursor()
#     c.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, pdf_hash TEXT, note TEXT)")
#     c.execute("CREATE TABLE IF NOT EXISTS processed_pdfs (hash TEXT PRIMARY KEY, text TEXT, summary TEXT)")
#     conn.commit()
#     conn.close()

# def save_note_to_db(note, pdf_hash):
#     conn = sqlite3.connect(DB_NAME)
#     c = conn.cursor()
#     c.execute("INSERT INTO notes (pdf_hash, note) VALUES (?, ?)", (pdf_hash, note))
#     conn.commit()
#     conn.close()

# def get_saved_notes(pdf_hash):
#     conn = sqlite3.connect(DB_NAME)
#     c = conn.cursor()
#     c.execute("SELECT note FROM notes WHERE pdf_hash=?", (pdf_hash,))
#     notes = [row[0] for row in c.fetchall()]
#     conn.close()
#     return notes

# def save_processed_pdf(pdf_hash, pdf_text, summary):
#     conn = sqlite3.connect(DB_NAME)
#     c = conn.cursor()
#     c.execute("INSERT INTO processed_pdfs (hash, text, summary) VALUES (?, ?, ?)", (pdf_hash, pdf_text, summary))
#     conn.commit()
#     conn.close()

# def get_processed_pdf(pdf_hash):
#     conn = sqlite3.connect(DB_NAME)
#     c = conn.cursor()
#     c.execute("SELECT text, summary FROM processed_pdfs WHERE hash=?", (pdf_hash,))
#     result = c.fetchone()
#     conn.close()
#     return result


import os
from supabase import create_client, Client
from supabase.client import ClientOptions

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(
    url, 
    key,
    options=ClientOptions(
        postgrest_client_timeout=10,
        storage_client_timeout=10,
        schema="public",
    )
)


