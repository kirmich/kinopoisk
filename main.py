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
db_film = []
type_obj = None

with open("spisok.txt", "r") as file:
    for line in file:
        if line[25:29] == 'film':
            spisok_film.append(line[30:-2])
        if line[25:31] == 'series':
            spisok_film.append(line[32:-2])

cache = {}

try:
    # try:
    with open('cache1.json', 'r') as f:
        cache = json.loads(f.read())
    # except FileNotFoundError:
    #     with open('cache1.json', 'w') as f:
    #         f.write('{}')
except json.decoder.JSONDecodeError:
    time.sleep(0.5)
ch = 0
for film_id in spisok_film:
    # ch = ch + 1
    # if ch > 5:
    #     break
    if str(film_id) in cache:
        data = {}
        for a in cache[str(film_id)]:
            data[a] = cache[str(film_id)][a]

        # print(data)

    else:
        data = {}
        # print('из реквеста:')
        req = requests.get(kinopoisk.API + 'films/' + str(film_id), headers=kinopoisk.headers)
        print('requests: ', req)
        request_json = json.loads(req.text)
        cache[str(film_id)] = request_json['data']
        rate_request = requests.get(f'https://rating.kinopoisk.ru/{film_id}.xml').text
        try:
            cache[str(film_id)]['kp_rate'] = xml.fromstring(rate_request)[0].text
        except:
            cache[str(film_id)]['kp_rate'] = None
        try:
            cache[str(film_id)]['imdb_rate'] = xml.fromstring(rate_request)[1].text
        except:
            cache[str(film_id)]['imdb_rate'] = None
        # print(cache[str(film_id)])
        data = cache[str(film_id)]
        time.sleep(1)


        with open('cache1.json', 'w') as f:
            json.dump(cache, f, indent=4)

    if data['type'] == "FILM":
        type_obj = "Фильм"
    elif data['type'] == "TV_SERIES":
        type_obj = "Сериал"

    # print(data)
    genres = []
    country = []

    for i in data['genres']:
        genres.append(i['genre'])

    for i in data['countries']:
        country.append(i['country'])

    data_film = [type_obj,
                 film_id,
                 data['kp_rate'],
                 data['imdb_rate'],
                 data['nameRu'],
                 data['nameEn'],
                 data['year'],
                 len(data['seasons']),
                 data['filmLength'],
                 ', '.join(genres),
                 ', '.join(country),
                 data['posterUrl'],
                 data['description'],
                 ]

    db_film.append(data_film)
    print('Выполнено', len(db_film), 'из', len(spisok_film), )



# print(db_film)

col = ['Фильм/Сериал',
       'КП id',
       'Кинопоиск',
       'IMDB',
       'Название',
       'Оригинальное название',
       'Год',
       'Кол-во сезонов',
       'Продолжительность',
       'Жанр',
       'Страна',
       'Постер',
       'Описание',
       ]
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_colwidth', 20)
# pd.set_option('display.max_columns', )
df_film = pd.DataFrame(db_film, columns=col)
df_film.to_excel('./film_new.xlsx')
print(df_film)
print(time.time() - start)