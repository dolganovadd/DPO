from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_links(url):
    try:
        with urlopen(url) as response:
            html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find_all('a')
        unique_links = set()
        for link in links:
            href = link.get('href')
            if href:
                unique_links.add(href)  
        return sorted(unique_links)  
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []

url_to_check = "https://en.wikipedia.org/wiki/Python"
links = get_links(url_to_check)

for link in links:
    print(link)