import requests #요청을 위한 라이브러리
import bs4  #파싱을 위한 라이브러리
from bs4 import BeautifulSoup

url = 'https://www.naver.com'

selectCode = '.ah_l .ah_item .ah_a .ah_k'

response = requests.get(url).text

soup = bs4.BeautifulSoup(response, 'html.parser')   #파싱하기위한 코드
rank = soup.select(selectCode)  #아이디값으로 접근해서 text를 꺼내오라는 명령


#print(rank)

for i in range(len(rank)):
    print(str(i+1)+' '+rank[i].text)



