# -*- coding: utf-8 -*-
import requests
import csv
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/running/current.nhn'
response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
movie_section = soup.select(
    '#content > .article > .obj_section > .lst_wrap > ul > li')

# print(len(movie_section)) 133

movies_list = []

for movie in movie_section:
    a_tag = movie.select_one('dl > dt > a')
    
    movie_title = a_tag.contents[0]
    movie_code = a_tag['href'].split('code=')[1]
    
    movie_data = {
        'title' : movie_title,
        'code' : movie_code
    }
    # movies_list.append(movie_data)
# print(movies_list)
    

