from bs4 import BeautifulSoup

def parse_items(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")
    items = []

    for card in soup.select(".item"):
        title = card.select_one(".title")
        price = card.select_one(".price")

        items.append({
            "title": title.get_text(strip=True) if title else None,
            "price": price.get_text(strip=True) if price else None
        })

    return items
