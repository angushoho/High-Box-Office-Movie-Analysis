import json
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from requests_html import HTMLSession

def change_money(str):
    try:
        money = int(str.replace(',', ''))
        return money
    except Exception as e:
        str = str.replace(',', '')
        for i in str:
            if i.isalpha():
                str.replace(i, '')

''' get ranking list '''
wiki_url = 'https://en.wikipedia.org/wiki/List_of_highest-grossing_films'
session = HTMLSession()
response = session.get(wiki_url)
titles = response.html.find('.wikitable')[0].find('i')
ranking_list = []
for title in titles:
    ranking_list.append(title.text)

''' get IMDb data '''
api_key = '2455a527'
year = ''
plot = 'full'

IMDb_rating = []
for title in ranking_list:
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

''' using pandas '''
movie_series = pd.Series(ranking_list, index=IMDb_rating)

dict = {'title': ranking_list, 'rating': IMDb_rating}
movie_frame = pd.DataFrame(dict)
print(movie_frame.head())

''' money list '''
money_list = []
box_office = response.html.find('.wikitable')[0].find('tbody [align=right]')
# print(box_office)
for money in box_office:
    m = change_money(money.text.split('$')[1])
    money_list.append(m)
# print(money_list)

plt.figure(figsize=(10, 6))
plt.scatter(movie_frame['rating'], money_list)
plt.xlabel('IMDb\'s rating')
plt.ylabel('box office')
plt.show()



''' figure: box office & rating scatter '''
'''
plt.figure(figsize=(10, 6))
plt.scatter(range(50), movie_frame['rating'])
plt.xlabel('ranking')
plt.ylabel('rating')
plt.show()
'''

''' figure: box office & rating bar '''
'''
ranking_statistics = [0] * 10
print(IMDb_rating)
for rating in IMDb_rating:
    try:                                         # in case of None value
        # rating_int = int(rating)
        rating_int = round(rating)
        ranking_statistics[rating_int - 1] += 1
    except Exception as e:
        pass
rate = list(range(1, 11))
plt.bar(rate, ranking_statistics)
plt.xticks(rate, rate)
plt.show()
'''


''' inflation  '''
titles = response.html.find('.wikitable')[1].find('i')
ranking_list_inflation = []
for title in titles:
    ranking_list_inflation.append(title.text)
# print(ranking_list_inflation)
money_list = []
box_office = response.html.find('.wikitable')[1].find('tbody td .sortkey')
for money in box_office:
    money_list.append(money.text.split('$')[1])
api_key = '2455a527'
year = ''
plot = 'full'

rating_inflation = []
for title in ranking_list_inflation:
    url = 'http://www.omdbapi.com/?t=' + title + '&y=' + year + 'plot=' + plot + '&apikey=' + api_key
    r = requests.get(url)
    try:
        data = json.loads(r.text)
        score = data['Ratings'][0]['Value']
        score = str(score).split('/')[0]
        score = float(score)
        rating_inflation.append(score)
        # print(score)
    except Exception as e:
        rating_inflation.append(None)
        # print(url)

# print(rating_inflation)

'''
plt.figure(figsize=(10, 6))
plt.scatter(rating_inflation, money_list)
plt.xlabel('ranking')
plt.ylabel('money (with infaltion)')
plt.show()
'''
