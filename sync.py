import urllib.request
import urllib.error
import os
import time

SUBS = {
    "cp-001.txt": "https://warp-gen.cyb-portal.org/CP-001",
    "cp-002.txt": "https://warp-gen.cyb-portal.org/CP-002",
    "cp-035.txt": "https://warp-gen.cyb-portal.org/CP-035",
    "cp-006.txt": "https://warp-gen.cyb-portal.org/CP-006",
    "cp-008.txt": "https://warp-gen.cyb-portal.org/CP-008",
    "cp-042.txt": "https://warp-gen.cyb-portal.org/CP-042",
}

for filename, url in SUBS.items():
    print(f"=====================================")
    print(f"Downloading {url}...")
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    )
    
    max_retries = 5
    success = False
    
    for attempt in range(1, max_retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                content = response.read().decode('utf-8').strip()
                
                # Проверка, чтобы случайно не сохранить ошибку Cloudflare или 404 страницу портала
                if len(content) > 10 and ("vless://" in content or "vmess://" in content or content.startswith("ey")):
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"[{attempt}/{max_retries}] Success! Saved to {filename} ({len(content)} bytes)")
                    success = True
                    break # Выходим из цикла попыток, так как скачали успешно
                else:
                    print(f"[{attempt}/{max_retries}] Validation failed. Content doesn't look like a valid subscription.")
                    
        except Exception as e:
            print(f"[{attempt}/{max_retries}] Error downloading: {e}")
            
        if attempt < max_retries:
            print(f"Waiting 5 seconds before retry...")
            time.sleep(5)
            
    if not success:
        print(f"Failed to fetch {filename} after {max_retries} attempts. Keeping the old file (if any).")
