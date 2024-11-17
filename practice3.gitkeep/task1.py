from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

def check_webpage(url):
    try:
        response = urlopen(url)
        print(f"Страница '{url}' найдена! Код ответа: {response.getcode()}")
    except HTTPError as e:
        print(f"HTTP ошибка: {e.code} - Страница '{url}' не найдена.")
    except URLError as e:
        print(f"Ошибка URL: {e.reason} - Убедитесь, что сервер доступен или URL корректен.")
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")

url_to_check = "https://pstu.ru/"
check_webpage(url_to_check)