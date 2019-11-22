import requests
import json
from pprint import pprint
api_key = '4da4b6d8f14f923557de5efc46603743'

movie_ids = []
with open('data/movie_id.txt', 'r') as f:
    for el in f.readlines():
        movie_ids.append(el.strip('\n'))

genre_dict = {}
i = 0
for movie_id in movie_ids:
    i += 1
    print(i)
    url = 'https://api.themoviedb.org/3/movie/{}?api_key={}&language=ko-KR'.format(movie_id, api_key)
    r = requests.get(url)
    data = json.loads(r.text)
    # pprint(data)
    # pprint(data['genres'][0]['id'])
    for genre in data['genres']:
        if genre['id'] in genre_dict.keys():
            continue
        else:
            genre_dict[genre['id']] = genre['name']

genre_list = []
for k, v in genre_dict.items():
    genre_list.append(
        {
            "pk": "{}".format(k),
            "model": "movies.genre",
            "fields": {
                "name": "{}".format(v)
            }
        }
    )

with open("genre.json", "w", encoding='utf-8') as json_file:
    json.dump(genre_list, json_file, ensure_ascii=False)
