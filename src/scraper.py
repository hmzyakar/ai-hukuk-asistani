# This module will be responsible for all web scraping tasks.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime

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
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = None
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(gazette_url)
        
        # Wait for the target elements to be present
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'fihrist-item')))
        
        # Find all div elements with class="fihrist-item"
        fihrist_elements = driver.find_elements(By.CLASS_NAME, 'fihrist-item')
        
        # Create list to store final URLs
        regulation_links = []
        
        # Iterate through each fihrist-item element
        for element in fihrist_elements:
            # Find the first anchor tag inside this element
            try:
                anchor = element.find_element(By.TAG_NAME, 'a')
                href = anchor.get_attribute('href')
                
                if href:
                    # The href should be a full, absolute URL
                    regulation_links.append(href)
            except:
                # No anchor found in this element, continue
                continue
        
        return regulation_links
        
    except Exception as e:
        print(f"Error fetching regulation links: {e}")
        return []
    finally:
        if driver:
            driver.quit()

def fetch_text_from_url(url):
    """Fetches the full, clean text content from a specific regulation's URL."""
    print(f"DEBUG: fetch_text_from_url called for {url}.")
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = None
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        
        # Wait for the content container to be present
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'content-container')))
        
        # Find the content container element
        content_element = driver.find_element(By.CLASS_NAME, 'content-container')
        text = content_element.text
        
        return text if text else ""
        
    except Exception as e:
        # If content-container not found, try RGT_MAIN as fallback
        try:
            main_elements = driver.find_elements(By.CLASS_NAME, 'RGT_MAIN')
            if not main_elements:
                print("No content elements found")
                return ""
            
            text_parts = []
            for element in main_elements:
                text = element.text
                if text:
                    text_parts.append(text)
            
            return ' '.join(text_parts)
            
        except Exception as fallback_e:
            print(f"Error fetching text from URL: {e}, Fallback error: {fallback_e}")
            return ""
    finally:
        if driver:
            driver.quit()