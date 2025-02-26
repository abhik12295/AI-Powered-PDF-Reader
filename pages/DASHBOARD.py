import streamlit as st
import os
from db import db_manager
from pdfminer.high_level import extract_text
import hashlib
import time
import base64
from supabase import create_client, Client

SUPABASE_URL = "SUPABASE_URL"
SUPABASE_KEY = "SUPABASE_KEY"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="📄 AI PDF Assistant", layout="wide")