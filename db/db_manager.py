import os
import json
import hashlib
import http.client
from pdfminer.high_level import extract_text
from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def generate_pdf_hash(pdf_file):
    md5_hash = hashlib.md5()
    while chunk := pdf_file.read(4096):
        md5_hash.update(chunk)
    pdf_file.seek(0)
    return md5_hash.hexdigest()

def get_user_pdfs(user_id):
    response = supabase.table("user_pdfs").select("*").eq("user_id", user_id).execute()
    return response.data if response.data else []

def get_user_pdf(user_id, pdf_hash):
    response = supabase.table("user_pdfs").select("*").eq("user_id", user_id).eq("pdf_hash", pdf_hash).execute()
    return response.data[0] if response.data else None

def save_user_pdfs(user_id, pdf_name, pdf_hash, extracted_text, summary):
    print(f"Saving PDF for user_id: {user_id}")  # Debugging
    if not user_id:
        print("Error: user_id is None or missing")
        return False
    
    existing_pdfs = get_user_pdfs(user_id)
    if len(existing_pdfs)>5:
        return False


    data = {
        "user_id" : user_id,
        "pdf_name" : pdf_name,
        "pdf_hash" : pdf_hash,
        "extracted_text" : extracted_text,
        "summary" : summary,
        #"created_at": "now()" 
    }

    #user_id = user.id  # Ensure this is passed to `save_user_pdfs`
    print(f"Authenticated User ID: {user_id}")

    try:
        if data["user_id"]:
            print(f"user id is {data['user_id']}")
            response = supabase.table("user_pdfs").insert(data).execute()
            print("response", response)
            return response.data is not None
    except Exception as e:
        print(f"{e}")

def delete_user_pdf(user_id, pdf_hash):
    response = supabase.table("user_pdfs").delete().eq("user_id", user_id).eq("pdf_hash", pdf_hash).execute()
    return response.data is not None

def rename_user_pdf(user_id, pdf_hash, new_name):
    response = supabase.table("user_pdfs").update({"pdf_name": new_name}).eq("user_id", user_id).eq("pdf_hash", pdf_hash).execute()
    return response.data is not None

def save_user_note(user_id, pdf_hash, note):
    data = {
        "user_id" : user_id,
        "pdf_hash" : pdf_hash,
        "note" : note,
        "created_at" : "now()"
        }
    
    response =supabase.table("user_notes").insert(data).execute()
    return response.data is not None

def get_user_note(user_id, pdf_hash):
    response = supabase.table("user_notes").select("note").eq("user_id", user_id).eq("pdf_hash", pdf_hash).execute()
    return [note['note'] for note in response.data] if response.data else []

def extract_text_from_pdf(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception as e:
        return f"Error extracting text : {e}"

def chat_with_gpt(prompt, pdf_text):
    conn = http.client.HTTPSConnection("gpt-4o.p.rapidapi.com")
    payload = json.dump({
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

    conn.request("POST","/chat/completion", payload, headers)
    res = conn.getresponse()
    data = res.read()
    
    try:
        response = json.loads(data.decode("utf-8"))
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"
    

def generate_summary(pdf_text):
    """Generate an AI-powered summary of the PDF."""
    conn = http.client.HTTPSConnection("gpt-4o.p.rapidapi.com")
    
    payload = json.dumps({
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "Summarize the following PDF content succinctly."},
            {"role": "user", "content": pdf_text}
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
    
    response_json = json.loads(data.decode("utf-8"))
    return response_json.get("choices", [{}])[0].get("message", {}).get("content", "Error in generating summary.")

    