import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Target URL
BASE_URL = "https://www.ifreesite.com/bopomofo-edu-2.htm"
DOWNLOAD_DIR = "downloads"

# Headers to mimic a real browser and avoid 403 Forbidden
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def setup_download_dir():
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
        print(f"Created directory: {DOWNLOAD_DIR}")
    else:
        print(f"Directory already exists: {DOWNLOAD_DIR}")

def download_file(url, filename):
    try:
        print(f"Downloading {filename} from {url}...")
        response = requests.get(url, headers=HEADERS, stream=True)
        response.raise_for_status()
        
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Successfully downloaded: {filename}")
        return True
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
        return False

def main():
    setup_download_dir()
    
    print(f"Fetching page: {BASE_URL}")
    try:
        response = requests.get(BASE_URL, headers=HEADERS)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching page: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # The user provided a very specific selector path, but we want to capture all similar MP3 links.
    # Pattern observed: //00.ifreesite.com/bopomo-im/syb/*.mp3
    # We will look for all <a> tags whose href ends with .mp3 and contains "bopomo-im/syb"
    
    mp3_links = []
    
    # Strategy 1: Find all links and filter
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.endswith('.mp3') and 'bopomo-im/syb' in href:
            full_url = urljoin(BASE_URL, href)
            # Fix for protocol relative URLs (starting with //)
            if full_url.startswith("https:////"):
                 full_url = full_url.replace("https:////", "https://")
            elif full_url.startswith("http:////"):
                 full_url = full_url.replace("http:////", "http://")
            
            mp3_links.append(full_url)

    # Strategy 2: If the generic strategy misses, we could try the specific selector, 
    # but normally the generic one is better for bulk downloading similar items on a page.
    # The user pointed to: #io_container ... td:nth-child(3) > a
    # Let's verify if we found anything.
    
    print(f"Found {len(mp3_links)} MP3 links.")
    
    for url in mp3_links:
        # Extract filename from URL
        filename = os.path.basename(urlparse(url).path)
        download_file(url, filename)
        # Be nice to the server
        time.sleep(0.5)

    print("All downloads processed.")

if __name__ == "__main__":
    main()
