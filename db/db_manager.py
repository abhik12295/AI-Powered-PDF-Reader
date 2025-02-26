import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_user_pdfs(user_id):
    # fetch all pdfs for user
    response = supabase.table("user_pdfs").select("*").eq("user_id", user_id).execute()
    return response.data if response.data else []

def get_user_pdf(user_id, pdf_hash):
    #fetch specific pdf by hash for a user
    response = supabase.table("user_pdfs").select("*").eq("user_id", user_id).eq("pdf_hash", pdf_hash).execute()
    return response.data[0] if response.data else None

def save_user_pdfs(user_id, pdf_name, pdf_hash, extracted_text, summary):
    existing_pdfs = get_user_pdf(user_id)
    if len(existing_pdfs)>=5:
        return False
    
    data = {
        "user_id": user_id,
        "pdf_name": pdf_name,
        "pdf_hash": pdf_hash,
        "extracted_text": extracted_text,
        "summary": summary,
        "created_at": "now()"
    }
    response = supabase.table("user_pdfs").insert(data).execute()
    return response.data is not None

def delete_user_pdf(user_id, pdf_hash):
    supabase.table("user_pdfs").delete().eq("user_id", user_id).eq("pdf_hash", pdf_hash).execute()

def rename_user_pdf(user_id, pdf_hash, new_name):
    supabase.table("user_pdfs").update({"pdf_name": new_name}).eq("user_id", user_id).eq("pdf_hash", pdf_hash).execute()
    

