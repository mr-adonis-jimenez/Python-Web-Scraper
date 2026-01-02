import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; DataScraper/1.0)"
}

def fetch_html(url: str) -> str:
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.text
