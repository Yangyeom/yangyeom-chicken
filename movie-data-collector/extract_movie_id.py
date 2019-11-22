import requests
import json
from pprint import pprint
api_key = '4da4b6d8f14f923557de5efc46603743'

tmp_list = []
for i in range(1, 2):
    # popular movies
    url = 'https://api.themoviedb.org/3/movie/popular?api_key={}&language=ko-KR&page={}'.format(api_key, i)
    r = requests.get(url)
    data = json.loads(r.text)
    for el in data['results']:
        tmp_list.append(el['id'])

with open('data/movie_id_tmp.txt', 'w') as f:
    for item in tmp_list:
        f.write("%s\n" % item)

# http://image.tmdb.org/t/p/w185/zephyR9sWnscPjadlDhWXPWosmV.jpg
