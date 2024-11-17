import requests
from bs4 import BeautifulSoup

def get_header(url):
    r = requests.get(url)
    bsh = BeautifulSoup(r.text, "html.parser")
    header1 = bsh.h1
    print(header1)

url_to_check = "https://www.example.com/"
get_header(url_to_check)
