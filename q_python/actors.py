import csv
from statistics import mean
from collections import Counter


def read(path):
    with open(path, encoding="utf-8") as file:
        actors = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = actors
        arr = []
        for index in range(len(data)):
            dict = {}
            for header_index in range(len(header)):
                dict[header[header_index]] = data[index][header_index]
            arr.append(dict)
    return arr


# Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.
def highest_movies(data):
    act = {}
    movies = 0
    for actor in data:
        if int(actor['Number of Movies']) > movies:
            act = {
                'Actor': actor['Actor'],
                'Number of Movies': int(actor['Number of Movies'])
            }
            movies = int(actor['Number of Movies'])
    return act


# Apresente a média da coluna contendo o número de filmes.
def average_films(data):
    return mean([int(actor['Number of Movies']) for actor in data])


# Apresente o nome do ator/atriz com a maior média por filme.
def actor_with_highest_average_per_movie(data):
    i = sorted(list(map(lambda x: float(x['Average per Movie']), data)))[-1:]
    for actor in data:
        if float(actor['Average per Movie']) == i[0]:
            return actor['Actor']


#  Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
def repeated_films(data):
    return Counter([actor['#1 Movie'] for actor in data]).most_common(1)[0]


data = read('q_python/actors.csv')
print(data[0])
print(highest_movies(data))
print(average_films(data))
print(actor_with_highest_average_per_movie(data))
print(repeated_films(data))
