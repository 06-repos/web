# -*- coding: utf-8 -*-
import requests
import csv
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/running/current.nhn'
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
a_list = soup.select(
    'dl[class=lst_dsc] > dt > a'
)
# a에 접근해서 해당 a들만 모아온다

for a in a_list:
    movie_title = a.text # <> 괄호 밖 텍스트만 불러온다
    # movie_code = a['href'].split('code=')[1]
    movie_code = a['href']
    movie_code = movie_code[movie_code.find('code=') + len('code='):]
    
    # csv 파일 만들기
    
    movie_data = {
        'title' : movie_title,
        'code' : movie_code
    }
    
    with open('./naver_movie.csv', 'a') as csvfile:
        fieldnames = ['title', 'code']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        csvwriter.writerow(movie_data)
        


    

