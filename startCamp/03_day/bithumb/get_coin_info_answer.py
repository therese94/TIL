import requests
import bs4
import csv

# 1. Bithumb  페이지를 가지고 온다.
response = requests.get('https://www.bithumb.com/')
html = response.text                #응답받은 객체에서 html문서를 string으로 가지고옴

# 2. Beautiful Soup 모듈을 이용하여 string type 의 html을 파싱한다.
soup = bs4.BeautifulSoup(html, 'html.parser')


# 3. 각 코인의 정보 담겨있는 table row 데이터를 list의 형태로 가져온다.
coins = soup.select('.coin_list tr')

# 4. 각 코인을 순회하며 필요한 정보만 추출한다.
for coin in coins:
    coin_name = coin.select_one('td:nth-child(1) > p > a > strong').text.replace('NEW','').strip()
    coin_price = coin.select_one('td:nth-child(2) > strong').text
    data = (coin_name, coin_price)
    csv_writer.writerow(data)                   # import csv 해야 쓸수 있는 함수