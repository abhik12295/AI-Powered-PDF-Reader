# import os
# from supabase import create_client, Client
# from dotenv import load_dotenv

# load_dotenv()
# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# create_table_query = """
# CREATE TABLE IF NOT EXISTS user_pdfs (
#     id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
#     user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
#     pdf_name TEXT NOT NULL,
#     pdf_hash TEXT UNIQUE NOT NULL,
#     extracted_text TEXT NOT NULL,
#     summary TEXT NULL,
#     created_at TIMESTAMP DEFAULT now()
# );
# """

# response = supabase.rpc("sql", {"query": create_table_query})
# print("Table Created Successfully!" if response else "Table Creation Failed.")

import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


# Check if env variables are loaded correctly
if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ ERROR: Missing Supabase URL or API Key. Check your .env file.")
    exit()

# Initialize Supabase Client
try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    response = supabase.table("test").select("*").execute()
    if response.data :
        print("✅ Supabase connection successful!")
        for row in response.data:
            print(row)
    else:
        print("⚠️ Connected, but no users found in test table.")
except Exception as e:
    print(f"❌ ERROR: Unable to connect to Supabase: {e}")
