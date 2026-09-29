import urllib.request
import urllib.error
import os

SUBS = {
    "cp-001.txt": "https://warp-gen.cyb-portal.org/CP-001",
    "cp-002.txt": "https://warp-gen.cyb-portal.org/CP-002",
    "cp-035.txt": "https://warp-gen.cyb-portal.org/CP-035",
    "cp-006.txt": "https://warp-gen.cyb-portal.org/CP-006",
    "cp-008.txt": "https://warp-gen.cyb-portal.org/CP-008",
    "cp-042.txt": "https://warp-gen.cyb-portal.org/CP-042",
}

for filename, url in SUBS.items():
    print(f"Downloading {url}...")
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            content = response.read().decode('utf-8').strip()
            
            # Проверка, чтобы случайно не сохранить ошибку Cloudflare или 404 страницу портала
            if len(content) > 10 and ("vless://" in content or "vmess://" in content or content.startswith("ey")):
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Saved to {filename} ({len(content)} bytes)")
            else:
                # Если контент не похож на подписку (например, портал вернул HTML-ошибку)
                # То мы просто пропускаем этот файл, и старая рабочая версия останется в репозитории
                print(f"Skipped {filename} - content validation failed.")
                
    except Exception as e:
        print(f"Error downloading {url}: {e}")
