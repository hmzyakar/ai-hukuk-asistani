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

## Prompt 2: Implement and Verify Dynamic URL Generation

**Part A: Implementation**

**File to Modify:** `src/scraper.py`

**Function to Implement:** `get_todays_gazette_url()`

**Requirements:**
1.  The function should no longer return a hardcoded placeholder URL.
2.  It needs to dynamically generate the URL for the **current date**.
3.  You must use the `datetime` class from Python's standard `datetime` library.
4.  Get the current year, month, and day.
5.  Format the date parts into the required string format for the URL. The structure is: `https://www.resmigazete.gov.tr/eskiler/YYYY/MM/YYYYMMDD.htm`
6.  Construct and return the final URL as a string.

**Example:**
If the current date is September 5, 2025, the function must return the exact string: "https://www.resmigazete.gov.tr/eskiler/2025/09/20250905.htm"

**Your Task:**
Please replace the entire existing `get_todays_gazette_url` function in `src/scraper.py` with the new, fully implemented version. Do not modify the other functions in the file yet.

**Part B: Verification**

1.  After modifying the function, create a temporary test file in the root directory (`/app`) named `test_runner.py`.
2.  Populate `test_runner.py` with the following content:
    ```python
    # test_runner.py
    import sys
    # Add the 'src' directory to the Python path to allow imports
    sys.path.insert(0, './src')
    
    from scraper import get_todays_gazette_url
    from datetime import datetime

    print("--- Running Verification Test ---")
    
    # Generate the expected URL manually for today's date
    today = datetime.now()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    expected_url = f"[https://www.resmigazete.gov.tr/eskiler/](https://www.resmigazete.gov.tr/eskiler/){year}/{month}/{year}{month}{day}.htm"

    # Call the function from the scraper module
    generated_url = get_todays_gazette_url()
    
    print(f"Expected URL: {expected_url}")
    print(f"Generated URL: {generated_url}")

    # Simple check
    if generated_url == expected_url:
        print("✅ Test PASSED: The function returned the correct URL.")
    else:
        print("❌ Test FAILED.")

    ```
3.  Execute this test file using the command: `python test_runner.py`
4.  Show me the full output of the execution.
5.  After the test is complete and you have shown the output, delete the temporary `test_runner.py` file to keep the project directory clean.