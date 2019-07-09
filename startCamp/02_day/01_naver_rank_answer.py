###########################답안 코드
import requests
import bs4

url = 'https://www.naver.com'
selector = '.ah_l .ah_item .ah_a .ah_k'

html = requests.get(url).text
soup = bs4.BeautifulSoup(html, 'html.parser')
rank = soup.select(selector)

#print(rank)

for ranks in rank:
    print(ranks.text)