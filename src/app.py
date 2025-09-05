# This is the main file for our Streamlit user interface.

import streamlit as st
# Imports are now correct for a script running inside the 'src' directory
from scraper import get_todays_gazette_url, fetch_regulation_links, fetch_text_from_url
from analyzer import setup_ai_model, summarize_and_categorize_text

st.set_page_config(page_title="AI Hukuk Asistanı", layout="wide")
st.title("⚖️ AI Hukuk Asistanı")
st.markdown("Günlük Resmî Gazete gündemini sizin için analiz eder ve özetler.")

# Setup the AI model once
model = setup_ai_model()

st.divider()

if st.button("Bugünün Gündemini Getir"):
    if not model:
        st.error("AI model could not be initialized. Please check your API key in the .env file.")
    else:
        # Step 1: Get today's gazette URL
        with st.spinner("Bugünkü Resmî Gazete URL'i alınıyor..."):
            gazette_url = get_todays_gazette_url()
            if not gazette_url:
                st.error("Bugünkü Resmî Gazete URL'i oluşturulamadı.")
                st.stop()

        st.info(f"Scraping this URL for links: {gazette_url}")
        
        # Step 2: Fetch regulation links from the gazette page
        with st.spinner("Düzenleme linkler aranıyor..."):
            regulation_links = fetch_regulation_links(gazette_url)
            
            if not regulation_links:
                st.warning("Bugün Resmî Gazete'de analiz edilecek yeni bir düzenleme bulunamadı.")
                st.stop()
            
            st.success(f"Toplam {len(regulation_links)} düzenleme bulundu.")
        
        # Step 3: Process each regulation
        for i, link_url in enumerate(regulation_links, 1):
            with st.spinner(f"Düzenleme {i}/{len(regulation_links)} analiz ediliyor..."):
                # Fetch the text content from the regulation URL
                regulation_text = fetch_text_from_url(link_url)
                
                if not regulation_text:
                    st.warning(f"Düzenleme {i}: Metin içeriği alınamadı.")
                    continue
                
                # Analyze the text using the AI model
                category, summary = summarize_and_categorize_text(model, regulation_text)
                
                # Display the results
                st.subheader(f"📋 Düzenleme {i}: {category}")
                st.markdown(f"**Özet:** {summary}")
                
                # Show the source link
                st.markdown(f"**Kaynak:** [Düzenleme metnini görüntüle]({link_url})")
                st.divider()
        
        st.success("🎉 Tüm düzenlemeler başarıyla analiz edildi!")