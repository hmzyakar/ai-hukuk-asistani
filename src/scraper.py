# This module will be responsible for all web scraping tasks.

import requests
from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

def get_todays_gazette_url():
    """Constructs the URL for today's Official Gazette."""
    print("DEBUG: get_todays_gazette_url called.")
    today = datetime.now()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    url = f"https://www.resmigazete.gov.tr/eskiler/{year}/{month}/{year}{month}{day}.htm"
    return url

def fetch_regulation_links(gazette_url):
    """Fetches all the links to new regulations from the main gazette page."""
    print(f"DEBUG: fetch_regulation_links called for {gazette_url}.")
    
    try:
        response = requests.get(gazette_url, headers=HEADERS)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        container = soup.find('div', class_='container-rgs')
        if not container:
            print("No container-rgs div found")
            return []
        
        links = []
        for link in container.find_all('a', href=True):
            href = link['href']
            if href:
                absolute_url = f"https://www.resmigazete.gov.tr/{href}"
                links.append(absolute_url)
        
        return links
        
    except Exception as e:
        print(f"Error fetching regulation links: {e}")
        return []

def fetch_text_from_url(url):
    """Fetches the full, clean text content from a specific regulation's URL."""
    print(f"DEBUG: fetch_text_from_url called for {url}.")
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        main_divs = soup.find_all('div', class_='RGT_MAIN')
        if not main_divs:
            print("No RGT_MAIN divs found")
            return ""
        
        text_parts = []
        for div in main_divs:
            text = div.get_text(separator=' ', strip=True)
            if text:
                text_parts.append(text)
        
        return ' '.join(text_parts)
        
    except Exception as e:
        print(f"Error fetching text from URL: {e}")
        return ""