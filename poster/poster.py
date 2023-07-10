import wget

list_poster = []


with open("poster.txt", "r") as file:
        for line in file:
            list_poster.append(line[0:-1])

for url in list_poster:
    wget.download(url, url[54:])
print('Done')