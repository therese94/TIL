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



if __name__ == '__main__':
    app.run(debug=True)
