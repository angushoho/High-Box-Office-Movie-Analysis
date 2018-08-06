from requests_html import HTMLSession
import requests



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
for title in rating_list:
    url = 'http://www.omdbapi.com/?t=' + title + '&y=' + year + 'plot=' + plot + '&apikey=' + api_key
    r = requests.get(url)
    try:
        data = json.loads(r.text)
        score = data['Ratings'][0]['Value']
        score = str(score).split('/')[0]
        score = float(score)
        IMDb_rating.append(score)
    except Exception as e:
        IMDb_rating.append(None)

print(IMDb_rating)
