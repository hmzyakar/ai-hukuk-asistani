# This module will handle all interactions with the AI model.

import os
from dotenv import load_dotenv
import google.generativeai as genai

def setup_ai_model():
    """Loads the API key and configures the Gemini model."""
    print("DEBUG: setup_ai_model called.")
    
    try:
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        
        if not api_key or api_key.strip() == "" or api_key.strip() == "PASTE_YOUR_API_KEY_HERE":
            raise ValueError("GOOGLE_API_KEY not found in .env file. Please check your setup.")
        
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