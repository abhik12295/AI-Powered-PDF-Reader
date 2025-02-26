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

    # Fetch data from the user_pdfs table
    response = supabase.table("user_pdfs").select("*").limit(5).execute()

    if response.data:
        print("✅ Table exists and contains data:", response.data)
    else:
        print("⚠️ Table exists but has no data.")
except Exception as e:
    print(f"❌ ERROR: {e}")
