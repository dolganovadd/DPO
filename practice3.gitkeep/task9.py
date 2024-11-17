import requests
from bs4 import BeautifulSoup
import random

def scrape_imdb_top_movies():
    url = "https://www.imdb.com/chart/top"

    # Указываем User-Agent, чтобы имитировать браузер
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Запрос к странице IMDb
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка успешности запроса
        
        # Парсим страницу
        soup = BeautifulSoup(response.text, "html.parser")

        # Находим блоки с фильмами
        movies = []
        for row in soup.select('table.chart tbody tr'):
            title_column = row.find('td', class_='titleColumn')
            if title_column and title_column.a:
                title = title_column.a.text
                year = title_column.span.text.strip('()')
                description = title_column.a['title']  # Получаем описание из атрибута title
                movies.append((title, year, description))

        return movies
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []

def print_random_movies(movies, n=10):
    # Выбираем случайные фильмы
    random_movies = random.sample(movies, min(n, len(movies)))

    for title, year, description in random_movies:
        print(f"{title} ({year})")
        print(f"{description}\n" + "-" * 60)

if __name__ == "__main__":
    # Собираем фильмы
    movies = scrape_imdb_top_movies()
    
    if movies:
        # Печатаем 10 случайных фильмов
        print_random_movies(movies)
    else:
        print("Не удалось получить данные.")
