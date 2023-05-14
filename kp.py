from kinopoisk_api import KP
import requests
import pandas as pd
import json
import xml
import xml.etree.ElementTree as xml
import time
import os

start = time.time()

kinopoisk = KP(token='be5114b9-31c7-4d3d-b88e-874fb3cf8f11')
print(kinopoisk.about, kinopoisk.version)

spisok_film = []
data = []

with open("spisok.txt", "r") as file:
    for line in file:
        if line[25:29] == 'film':
            spisok_film.append(line[30:-2])
        if line[25:31] == 'series':
            spisok_film.append(line[32:-2])


# class CACHE:
#     def __init__(self):
#         self.PATH = os.path.dirname(os.path.abspath(__file__))
#
#     def load(self) -> dict:
#         try:
#             with open(self.PATH + '/cache.json', 'r') as f:
#                 return json.loads(f.read())
#         except FileNotFoundError:
#             with open(self.PATH + '/cache.json', 'w') as f:
#                 f.write('{}')
#                 return {}
#
#     def write(self, cache: dict, indent: int = 4):
#         with open(self.PATH + '/cache.json', 'w') as f:
#             return json.dump(cache, f, indent=indent)

def get_data(id):
    # cache = CACHE().load()
    genres =[]
    country = []
    type_obj = None

    req = requests.get(kinopoisk.API + 'films/' + str(id), headers=kinopoisk.headers)
    # print(req.text)

    if req.status_code != 200:
        b = []
        return b

    request = req.text
    covet = json.loads(request)

    # if str(id) in cache:
    #     print(cache[id])
    #
    # print(covet)
    #
    # cache[str(id)] = covet['data']
    # CACHE().write(cache)

    rate_request = requests.get(f'https://rating.kinopoisk.ru/{id}.xml').text
    kp_rate = xml.fromstring(rate_request)[0].text
    imdb_rate = xml.fromstring(rate_request)[1].text

    if covet['data']['type'] == "FILM":
        type_obj = "Фильм"
    elif covet['data']['type'] == "TV_SERIES":
        type_obj = "Сериал"




    for i in covet['data']['genres']:
        genres.append(i['genre'])


    for i in covet['data']['countries']:
        country.append(i['country'])

    data_film = [type_obj,
                 kp_rate,
                 imdb_rate,
                 covet['data']['nameRu'],
                 covet['data']['nameEn'],
                 covet['data']['year'],
                 len(covet['data']['seasons']),
                 covet['data']['filmLength'],
                 ', '.join(genres),
                 ', '.join(country),
                 covet['data']['description'],
                 ]
    return data_film

for i in spisok_film:
    data.append(get_data(i))

    print('Записан id', i)
    print('Завершено', round(((1 / len(spisok_film)) * len(data) * 100), 1), '%;  ', len(data), 'из', len(spisok_film),)
    end = time.time() - start
    print('Прошло', round(end, 2), 'сек.')
    # time.sleep(3)
    # if len(data) > 5:
    #     break

print('Информация собрана, записей - ', len(data))

col = ['Фильм?',
       'Кинопоиск',
       'IMDB',
       'Название',
       'Оригинальное название',
       'Год', 'Кол-во сезонов',
       'Продолжительность',
       'Жанр', 'Страна',
       'Описание',
       ]

df_film = pd.DataFrame(data, columns=col)
print(df_film)
df_film.to_excel('./film.xlsx')
print('Информация записана в файл')