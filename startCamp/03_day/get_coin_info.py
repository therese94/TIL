import requests
import bs4

url = 'https://www.bithumb.com/'
selector_name = '.coin_list tr td p strong'
selector_price = '.coin_list tr td .sort_real'

html = requests.get(url).text
soup = bs4.BeautifulSoup(html, 'html.parser')

coin_name = soup.select(selector_name)
coin_price = soup.select(selector_price)

x = []
y = []

for name in coin_name:
    # print(name.text)                                          ##여기는 확인용 프린트문
    x.append(name.text)

for price in coin_price:
    # print(price.text)                                         ##여기는 확인용 프린트문
    y.append(price.text)

# for i in range(len(coin_name)):                               ##여기는 확인용 프린트문
#     print(x[i].replace('NEW',''), y[i])

# for i in range(len(coin_name)):
#     x[i].replace(x[i].replace("NEW",""))                      ##이렇게 하면 원본을 변화시키는게 아니라서 NEW를 없앤 결과를 프린트할 수 없음 
    # print(x[i], y[i])                                         ##변수에 넣어서 프린트문에 넣어야함 or 위에 코딩한 것처럼 전체를 프린트문에 넣기

with open('write_coin_info.csv','w',encoding="utf-8") as f:
    for i in range(len(coin_name)):
        f.write(f'{x[i].replace("NEW","")}, {y[i]}\n')
