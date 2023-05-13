from kinopoisk_api import KP
import pandas as pd

kinopoisk = KP(token='be5114b9-31c7-4d3d-b88e-874fb3cf8f11')
print(kinopoisk.about, kinopoisk.version)

spisok = []

with open("spisok.txt", "r") as file:
    for line in file:
        if line[25:29] == 'film':
            print(line[30:-2])
            spisok.append(line[30:-2])
        else: print(line)

# data = []
#
# for i in spisok:
#     a = kinopoisk.get_film(i)
#     b = [a.ru_name,
#          a.name,
#          a.year,
#          a.duration,
#          a.genres,
#          a.countries,
#          a.kp_rate,
#          a.imdb_rate,
#          a.description]
#     data.append(b)
#
# col = ['Название', 'Оригинальное название', 'Год', 'Продолжительность', 'Жанр', 'Страна', 'Кинопоиск', 'IMDB', 'Описание']
#
# df = pd.DataFrame(data, columns=col)
#
# print(df)
#
# df.to_excel('./film.xlsx')

