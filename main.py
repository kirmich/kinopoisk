from kinopoisk_api import KP
import requests
import pandas as pd
import json
import xml
import xml.etree.ElementTree as xml
import time
import os

kinopoisk = KP(token='be5114b9-31c7-4d3d-b88e-874fb3cf8f11')
print(kinopoisk.about, kinopoisk.version)

film_id = 13767

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


if str(film_id) in cache:
    data = {}
    for a in cache[str(film_id)]:
        data[a] = cache[str(film_id)][a]
    print('из кэша:')
    print(data)

else:
    print('из реквеста:')
    req = requests.get(kinopoisk.API + 'films/' + str(film_id), headers=kinopoisk.headers)
    print('рек: ', req)
    request_json = json.loads(req.text)
    # print(request_json['data'])
    cache[str(film_id)] = request_json['data']
    print(cache[str(film_id)])
    print('кэш на запись:', cache[str(film_id)])
    with open('cache1.json', 'w') as f:
        json.dump(cache, f, indent=4)
