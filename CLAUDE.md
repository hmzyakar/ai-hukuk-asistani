# AI Hukuk Asistanı - Claude Code Görev Günlüğü

Bu dosya, projeyi geliştirmek için Claude Code'a verilen ana prompt'ları içerir.

---

## Prompt 1: Proje Başlangıcı ve Kurulum

You are an expert Python developer. Your primary task is to set up the initial file structure and boilerplate code for our "AI Legal Assistant" project inside a new `src` directory.

The development language is Python.

Please perform the following steps precisely:

**Step 1: Create the Project File Structure**

Create the following files and directories in the current working directory (`/app`):
- `.gitignore`
- `.env`
- `CLAUDE.md`
- `src/` (a directory named src)
- `src/__init__.py` (an empty file to make 'src' a Python package)
- `src/app.py`
- `src/scraper.py`
- `src/analyzer.py`

**Step 2: Populate the Initial Files**

Populate each of the newly created files with the following content exactly as specified.

**File: `.gitignore`**
Virtual Environment & Python cache
venv/
.venv/
env/
pycache/
*.pyc

Environment variables
.env

IDE and OS files
.idea/
.vscode/
*.DS_Store


**File: `.env`**
This file will hold our secret API key.
The user will paste their actual Google AI Studio API key here.
GOOGLE_API_KEY="PASTE_YOUR_API_KEY_HERE"


**File: `CLAUDE.md`**
```markdown
# AI Hukuk Asistanı - Claude Code Görev Günlüğü

Bu dosya, projeyi geliştirmek için Claude Code'a verilen ana prompt'ları içerir.

---

## Prompt 1: Proje Başlangıcı ve Kurulum

(Bu dosyanın oluşturulmasını isteyen prompt'un tamamı buraya eklenecek.)
(Claude'a Not: Bu markdown bloğunun içine, şu an sana verdiğim bu görevin tamamını (prompt'un tamamını) yapıştır.)

File: src/__init__.py
(This file should be created but remain empty.)

File: src/scraper.py

Python

# This module will be responsible for all web scraping tasks.

import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_todays_gazette_url():
    """Constructs the URL for today's Official Gazette."""
    print("DEBUG: get_todays_gazette_url called.")
    return "[https://www.resmigazete.gov.tr/eskiler/2025/09/05/20250905.htm](https://www.resmigazete.gov.tr/eskiler/2025/09/05/20250905.htm)" # Placeholder

def fetch_regulation_links(gazette_url):
    """Fetches all the links to new regulations from the main gazette page."""
    print(f"DEBUG: fetch_regulation_links called for {gazette_url}.")
    return [] # Placeholder

def fetch_text_from_url(url):
    """Fetches the full, clean text content from a specific regulation's URL."""
    print(f"DEBUG: fetch_text_from_url called for {url}.")
    return "Placeholder text for a regulation." # Placeholder
File: src/analyzer.py

Python

# This module will handle all interactions with the AI model.

import os
from dotenv import load_dotenv
import google.generativeai as genai

def setup_ai_model():
    """Loads the API key and configures the Gemini model."""
    print("DEBUG: setup_ai_model called.")
    load_dotenv()
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in .env file.")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        return model
    except Exception as e:
        print(f"Error setting up AI model: {e}")
        return None

def summarize_and_categorize_text(model, text_content):
    """Takes a chunk of legal text and uses the AI model to summarize and categorize it."""
    print("DEBUG: summarize_and_categorize_text called.")
    # TODO: Implement the expert legal prompt here.
    summary = "This is a placeholder summary."
    category = "Placeholder Category"
    return category, summary
File: src/app.py

Python

# This is the main file for our Streamlit user interface.

import streamlit as st
# Notice the change in imports due to the 'src' directory
from src.scraper import get_todays_gazette_url, fetch_regulation_links, fetch_text_from_url
from src.analyzer import setup_ai_model, summarize_and_categorize_text

st.set_page_config(page_title="AI Hukuk Asistanı", layout="wide")
st.title("⚖️ AI Hukuk Asistanı")
st.markdown("Günlük Resmî Gazete gündemini sizin için analiz eder ve özetler.")

# Setup the AI model once
model = setup_ai_model()

st.divider()

if st.button("Bugünün Gündemini Getir"):
    st.info("Fetching today's agenda... (This is a placeholder action)")
    
    if model:
        # TODO:
        # 1. Call scraper functions to get texts.
        # 2. For each text, call analyzer functions.
        # 3. Display results.
        st.success("Analysis complete!")
    else:
        st.error("AI model could not be initialized. Please check your API key in the .env file.")
Step 3: Final Confirmation

After creating all the files and their contents, please confirm by running the tree /F command and showing me the output.