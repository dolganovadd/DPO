import requests

def check_ssl(url):
    try:
        r= requests.get(url)
        print ("У сайта есть SSL сертификат")
    except requests.exceptions.SSLError:
        print ("У сайта нет SSL сертификата")

url_to_check = "https://pstu.ru/"
check_ssl(url_to_check)