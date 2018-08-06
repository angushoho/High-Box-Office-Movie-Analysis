from requests_html import HTMLSession
import requests
import json


''' get ranking list '''
imdb_url = 'https://www.imdb.com/chart/top'
session = HTMLSession()
response = session.get(imdb_url)
titles = response.html.find('.chart tbody .titleColumn a')

rating_list = []
for title in titles:
    rating_list.append(title.text)


''' get box office '''


api_key = '2455a527'
year = ''
plot = 'full'

IMDb_rating = []
rotten_tomato_rating = []
json_data = {}
for title in rating_list:
    url = 'http://www.omdbapi.com/?t=' + title + '&y=' + year + 'plot=' + plot + '&apikey=' + api_key
    r = requests.get(url)
    # print(r.text)
    data = json.loads(r.text)
    try:
        score = data['Ratings'][0]['Value']
        score = score.split('/')[0]
        score = float(score)
        IMDb_rating.append(score)
    except Exception as e:
        IMDb_rating.append(None)

    try:
        score_r = data['Ratings'][1]['Value']
        score_r = score_r.split('%')[0]
        score_r = float(score_r)
        rotten_tomato_rating.append(score_r)
    except Exception as e:
        rotten_tomato_rating.append(None)

print(rotten_tomato_rating)
