from scraper.fetcher import fetch_html
from scraper.parser import parse_items
from scraper.exporter import export_csv

def run(url: str):
    html = fetch_html(url)
    data = parse_items(html)
    export_csv(data, "data/output.csv")

if __name__ == "__main__":
    run("https://example.com/products")
