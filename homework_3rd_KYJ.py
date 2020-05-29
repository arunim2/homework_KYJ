import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#순위rank, 곡제목title, 가수singer

movies = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for movie in movies:    
    title = movie.select_one('td.info > a.title.ellipsis').text.strip()    
    singer = movie.select_one('td.info > a.artist.ellipsis').text.strip()
    spans = movie.select_one('td.number > span').text
    number = movie.select_one('td.number').text.strip(spans).strip()

    print(number, title, singer)
