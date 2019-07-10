from flask import Flask
import datetime
import random
app = Flask(__name__)


@app.route("/")                         ##앞에 @붙은건 decorator인데 일종의 함수 비슷한거  ##여기서 @app.route()는 endpoint 기능
def hello():
    return "Hello JUNE!"


@app.route('/ssafy')
def ssafy():
    return 'Hello SSAFY'


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    b_day = datetime.datetime(2019, 10, 13)
    td = b_day - today
    return f'{td.days}일 남았습니다.'


@app.route('/html')
def html():
    return '<h1>This is HTML</h1>'


@app.route('/html_lines')
def html_lines():
    return '''
    <h1>여러줄을 보내 봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
        <li>3번</li>
    </ul>
    '''

@app.route('/greeting/IU')
def greeting_IU():
    return '반갑습니다 IU님'


@app.route('/greeting/ziont')
def greeting_ziont():
    return '반갑습니다 ZionT님'


# Variable Routing
@app.route('/greeting/<name>')
def greeting(name):
    return f'반갑습니다. {name} 님' 


@app.route('/cube/<int:num>')
def cube(num):
    return f'{num}의 3 제곱은 {num ** 3}입니다.'

#실습
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['피자','파스타','떡볶이','짜장면','짬뽕','탕수육','볶음밥']
    order = random.sample(menu, people)
    return str(order)                       #리스트 타입은 return 할 수 없음


if __name__ == '__main__':
    app.run(debug=True)