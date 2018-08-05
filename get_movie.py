from requests_html import HTMLSession
from requests_html import requests
import json

api_key = '2455a527'
year = ''
plot = 'full'
title = 'Fight Club'

url = 'http://www.omdbapi.com/?t=' + title + '&y=' + year + 'plot=' + plot + '&apikey=' + api_key
r = requests.get(url)
data = json.loads(r.text)
data = json.dumps(data, indent=4)
print(data)
'''
try:
    data = json.loads(r.text)
    score = data['Ratings'][0]['Value']
    score = str(score).split('/')[0]
    score = float(score)
    
except Exception as e:
    # IMDb_rating.append(None)
    print(url)
'''