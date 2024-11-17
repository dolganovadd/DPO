import pandas as pd

def count_rows(url):
    try:
        df = pd.read_csv(url)
        row_count = df.shape[0]  
        print(f"Количество строк в файле: {row_count}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

url_to_check = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv"
count_rows(url_to_check)