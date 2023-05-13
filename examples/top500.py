from kinopoisk_api import KP

kinopoisk = KP(token='be5114b9-31c7-4d3d-b88e-874fb3cf8f11')

top500 = kinopoisk.top500()

for item in top500:
    print(item.ru_name, item.year)
    print(", ".join(item.genres))
    print(", ".join(item.countries))
