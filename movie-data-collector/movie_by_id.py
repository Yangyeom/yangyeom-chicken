import requests
import json
from pprint import pprint
api_key = '4da4b6d8f14f923557de5efc46603743'

movie_ids = []
with open('data/movie_id.txt', 'r') as f:
    for el in f.readlines():
        movie_ids.append(el.strip('\n'))

movie_list = []
pk = 1
for movie_id in movie_ids:
    print(pk)
    url = 'https://api.themoviedb.org/3/movie/{}?api_key={}&language=ko-KR'.format(movie_id, api_key)
    r = requests.get(url)
    data = json.loads(r.text)
    genre_tmp_list = []
    for genre in data['genres']:
        genre_tmp_list.append(genre['id'])
    movie_list.append({
        "pk": pk,
        "model": "movies.Movie",
        "fields": {
            "title": data['title'],
            "poster_url": data['poster_path'],
            "description": data['overview'],
            "genres": genre_tmp_list
        }
    })
    pk += 1


with open("movie.json", "w", encoding='utf-8') as json_file:
    json.dump(movie_list, json_file, ensure_ascii=False)