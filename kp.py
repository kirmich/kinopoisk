from kinopoisk_api import KP

kinopoisk = KP(token='be5114b9-31c7-4d3d-b88e-874fb3cf8f11')
print(kinopoisk.about, kinopoisk.version)

# spisok = []
#
# with open("spisok.txt", "r") as file:
#     for line in file:
#         spisok.append(line[30:-2])
#
# print(spisok)

tenet = kinopoisk.get_film('1236063')



