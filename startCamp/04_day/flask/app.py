from flask import Flask, render_template, request   # 사용자의 요청을 확인할 수 있는 객체 : 전에 사용했던 requests랑은 다름 - flask 자체에서 제공되는 것
import requests
import datetime
import random
app = Flask(__name__)


#가장 기본 도메인       ex) www.google.com          ex) www.google.com/search 이런식으로 root는 따로 지정
@app.route('/')
def index():
    return 'Hello world'


@app.route('/greeting/<string:name>')
def greeting(name):
    if name == 'june':
        return f'안녕하세요 {name}님'
    else:
        return '안녕'
    

@app.route('/cube/<int:num>')
def cube(num):
    return render_template('cube.html', html_num=num)


######################################### 예제 1 - PingPong
@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    age = request.args.get('age')
    return f'Pong! age: {age}'

###################################################################


######################################### 예제 2 - GOOGLE
@app.route('/google')
def google():
    return render_template('google.html')

##################################################################


######################################### 예제 3 - NAVER
@app.route('/naver')
def naver():
    return render_template('naver.html')

##################################################################


######################################### 예제 4 - ARTII 랜덤 출력
@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')


@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text') #Message
    #Ascii Art API를 활용해서 사용자의 input값을 변경한다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    result = response.text     # 그냥 response 프린트시 <Response [200]> 이라고 찍힘
    return render_template('ascii_result.html', result=result)

##################################################################


######################################### 예제 5 - 로또
@app.route('/lotto_input')              ##사용자가 입력할 수 있는 페이지를 보여주기
def lotto_input():
    return render_template('lotto_input.html')


@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('round')
    lotto_numbers = request.args.get('numbers').split()

    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)        #Json 타입(개발자가 특정 정보만 보고싶을때)으로 받게됨 <==> 사용자가 보기 편한건 html   ---?? 질문하기
    lotto_info = response.json()        #Json 타입의 파일을 python dictionary로 parsing해줘
    print(lotto_info)        

    ans_list = []

    for i in range(1,7):
        ans_list.append(str(lotto_info[f'drwtNo{i}']))

    ans_list.append(str(lotto_info['bnusNo']))

    
    ans_list.sort()
    print('=================================')
    print(ans_list)
    print(lotto_numbers)
    print('=================================')

    ans_num = 0

    for i in ans_list:
        if i in lotto_numbers:
            ans_num += 1

    print(ans_num)

    if ans_num == 6:
        rank = 1
    elif ans_num ==5:
        rank = 2
    elif ans_num ==4:
        rank = 3
    elif ans_num ==3:
        rank = 4
    elif ans_num ==2:
        rank = 5
    else:
        rank = 6

    # return f'{lotto_round}, {lotto_numbers}'
    return render_template('lotto_output.html',rank = rank, ans_num=ans_num, ans_list=ans_list, lotto_numbers=lotto_numbers)

if __name__ == '__main__':
    app.run(debug=True)
