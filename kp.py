from kinopoisk_api import KP
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

kinopoisk = KP(token='be5114b9-31c7-4d3d-b88e-874fb3cf8f11')

spisok_film = []
spisok_siries = []
with open("spisok.txt", "r") as file:
    for line in file:
        if line[25:29] == 'film':
            spisok_film.append(line[30:-2])
        if line[25:31] == 'series':
            spisok_siries.append(line[:-2])





data_f = []

for i in spisok_film:
    a = kinopoisk.get_film(i)
    b = [a.ru_name,
         a.name,
         a.year,
         a.duration,
         a.genres,
         a.countries,
         a.kp_rate,
         a.imdb_rate,
         a.description]
    data_f.append(b)

col = ['Название', 'Оригинальное название', 'Год', 'Продолжительность', 'Жанр', 'Страна', 'Кинопоиск', 'IMDB', 'Описание']

df_film = pd.DataFrame(data_f, columns=col)

print(df_film)

df_film.to_excel('./film.xlsx')

