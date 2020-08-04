import requests
from bs4 import BeautifulSoup, NavigableString, Tag

soup_objects = []

for i in range(1, 102, 10):

    base_url = https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=44&start=
    start_num =  i
    end_url = &refresh_start=0

    URL = base_url + str(url_num) + end_url

    response = requests.get(URL)
    soup = bs4.BeautifulSoup(response.text 'html.parcer')
    soup_objects.append(soup)

# 반복문으로 배열 돌면서 원하는 데이터 출력하기

news_section = soup.select(
    'div[id=wrap] > div[id=container] > div[id=contant] > div[id=main_pack] > div.news'
)

for news in news_section:
    a_tag = news.select_one('dl > dt > a')
    news_title = a_tag['title'] 
    news_link = a_tag['href']


contents = soup.select() # 

print(soup.)