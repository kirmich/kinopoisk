from kinopoisk_api import KP

kinopoisk = KP(token='be5114b9-31c7-4d3d-b88e-874fb3cf8f11')

tenet = kinopoisk.get_film(1236063)

print(tenet.ru_name, tenet.year)
print(", ".join(tenet.genres))
print(", ".join(tenet.countries))
print(tenet.tagline)