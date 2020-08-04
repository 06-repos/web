import requests
from bs4 import BeautifulSoup

# 설치와 작동에 대한 Test
response = requests.get{'https://www.naver.com'}

print(response.text)
