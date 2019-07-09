import requests
import bs4  #Beautiful Soup - third party library 이 라이브러리를 이용해서 html문서 내 원하는 정보 긁어올수 있음 - ex) html문서 내 요소의 유일한 값인 id로 

url = 'https://finance.naver.com/sise/'

response = requests.get(url)
html = response.text

print(type(html))
print(response)
print(response.status_code) #404같은 페이지 없음 등의 페이지 상태 코드 받기 / 정상적인 경우 코드는 200

soup = bs4.BeautifulSoup(html, 'html.parser')   #파싱하기위한 코드
kospi = soup.select_one('#KOSPI_now')  #아이디값으로 접근해서 text를 꺼내오라는 명령


print(kospi)
