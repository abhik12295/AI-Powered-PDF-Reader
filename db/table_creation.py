import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

create_table_query = """
CREATE TABLE IF NOT EXISTS user_pdfs (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    pdf_name TEXT NOT NULL,
    pdf_hash TEXT UNIQUE NOT NULL,
    extracted_text TEXT NOT NULL,
    summary TEXT NULL,
    created_at TIMESTAMP DEFAULT now()
);
"""

response = supabase.rpc("sql", {"query": create_table_query})
print("Table Created Successfully!" if response else "Table Creation Failed.")
