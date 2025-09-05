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
        response = requests.get(gazette_url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Get all anchor tags on the page
        all_anchors = soup.find_all('a')
        
        # Extract date string from the URL (e.g., '20250905')
        import re
        date_match = re.search(r'(\d{8})\.htm', gazette_url)
        if not date_match:
            print("Could not extract date from gazette URL")
            return []
        
        date_string = date_match.group(1)
        
        # Create list to store valid links
        valid_links = []
        
        # Iterate through each anchor tag
        for anchor in all_anchors:
            href = anchor.get('href')
            
            # Apply filtering logic: href must exist, contain date string, and end with .htm
            if href and date_string in href and href.endswith('.htm'):
                # Convert to absolute URL
                absolute_url = f"https://www.resmigazete.gov.tr/{href}"
                
                # Add to results list only if not already there (avoid duplicates)
                if absolute_url not in valid_links:
                    valid_links.append(absolute_url)
        
        return valid_links
        
    except Exception as e:
        print(f"Error fetching regulation links: {e}")
        return []

def fetch_text_from_url(url):
    """Fetches the full, clean text content from a specific regulation's URL."""
    print(f"DEBUG: fetch_text_from_url called for {url}.")
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
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