import os
import requests
import time

def download_files():
    # base_url = "https://www.mdnkids.com/bopomo/audio/{:02d}.mp3"
    # User requested range 01-37
    
    # Create directory for downloads
    save_dir = os.path.join(os.getcwd(), "mdn_audio")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print(f"Created directory: {save_dir}")
        
    for i in range(1, 38): # 1 to 37
        file_num = f"{i:02d}"
        url = f"https://www.mdnkids.com/bopomo/audio/{file_num}.mp3"
        filename = f"{file_num}.mp3"
        filepath = os.path.join(save_dir, filename)
        
        print(f"[{i}/37] Downloading {filename} from {url}...")
        
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"Success: Saved to {filepath}")
            else:
                print(f"Error: Status code {response.status_code} for {url}")
            
            # Sleep briefly to be polite to the server
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Exception while downloading {url}: {e}")

if __name__ == "__main__":
    download_files()

