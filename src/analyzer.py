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
    
    try:
        # Define the structured prompt for the Gemini model
        prompt = f"""
Sen Türk hukuku uzmanı bir avukatsın. Aşağıda verilen yasal metni analiz etmen gerekiyor.

Görevlerin:
1. Bu yasal metni uygun bir hukuk dalına kategorize et (örneğin: "Vergi Hukuku", "Ticaret Hukuku", "İcra ve İflas Hukuku", "İş Hukuku", "Medeni Hukuk", "Ceza Hukuku", vb.)
2. Bu düzenlemenin ne değiştirdiğini ve kimleri etkilediğini açıklayan tek paragraflık, sade bir özet yaz.

Lütfen cevabını tam olarak şu formatta ver:

Kategori: [Hukuk Dalı]
---
Özet: [Bir paragraflık özet metni]

Analiz edilecek yasal metin:
{text_content}
"""

        # Send the prompt to the Gemini model
        response = model.generate_content(prompt)
        
        # Extract the response text
        response_text = response.text.strip()
        
        # Parse the response to extract category and summary
        parts = response_text.split("---")
        if len(parts) >= 2:
            category_line = parts[0].strip()
            summary_text = parts[1].strip()
            
            # Extract category (remove "Kategori:" prefix)
            if category_line.startswith("Kategori:"):
                category = category_line.replace("Kategori:", "").strip()
            else:
                category = "Belirsiz"
            
            # Extract summary (remove "Özet:" prefix if present)
            if summary_text.startswith("Özet:"):
                summary = summary_text.replace("Özet:", "").strip()
            else:
                summary = summary_text
            
            return category, summary
        else:
            return "Belirsiz", "Analiz tamamlanamadı"
            
    except Exception as e:
        print(f"Error during text analysis: {e}")
        return "Error", "Analysis failed"