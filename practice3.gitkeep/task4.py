import requests

def get_text(url):
    try:
        r = requests.get(url)
        print(r.text)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")

url_to_check = "https://en.wikipedia.org/robots.txt"
get_text(url_to_check)