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