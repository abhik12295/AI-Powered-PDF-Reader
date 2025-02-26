import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ ERROR: Missing Supabase setup!")
    exit()

try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    response = supabase.table("user_pdfs").create([
        {"name": "id", "type": "uuid", "default": "gen_random_uuid()", "primary_key": True},
        {"name": "user_id", "type": "uuid", "references": "auth.users(id)", "on_delete": "CASCADE"},
        {"name": "pdf_name", "type": "text", "not_null": True},
        {"name": "pdf_hash", "type": "text", "unique": True, "not_null": True},
        {"name": "extracted_text", "type": "text", "not_null": True},
        {"name": "summary", "type": "text", "nullable": True},
        {"name": "created_at", "type": "timestamp", "default": "now()"}
    ])

    print("✅ Table Created Successfully!" if response else " ❌ Table Creation Failed.")
except Exception as e:
    print(f"ERROR: Unable to create table : {e}")