from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_all_headers(url):
    try:
        with urlopen(url) as response:
            html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        for header in headers:
            print(header.name, header.text.strip())
    except Exception as e:
        print(f"Произошла ошибка: {e}")

url_to_check = "https://en.wikipedia.org/wiki/Main_Page"
get_all_headers(url_to_check)
