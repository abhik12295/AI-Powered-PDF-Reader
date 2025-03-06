import streamlit as st
from supabase import  create_client, Client
import os, asyncio

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

async def sign_in_with_google():
    auth_response = await asyncio.to_thread(
        supabase.auth.sign_in_with_oauth, {"provider": "google"}
    )
    
    if hasattr(auth_response, "url"):
        return auth_response.url  # Correct way to access the URL
    
    raise ValueError("OAuth sign-in failed: No URL returned")

async def get_user_session():
    return await asyncio.to_thread(supabase.auth.get_user)

async def sign_out():
    await asyncio.to_thread(supabase.auth.sign_out)