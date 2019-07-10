from flask import Flask, render_template
import datetime
import random
app = Flask(__name__)


@app.route("/")                         ##앞에 @붙은건 decorator인데 일종의 함수 비슷한거  ##여기서 @app.route()는 endpoint 기능
def hello():
    return render_template('index.html')


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
    return render_template('greeting.html', html_name=name)         # html_name 에 name저장하고 넘겨주어 html에서 쓸 수 있도록 해줌


# @app.route('/cube/<int:num>')
# def cube(num):
#     return f'{num}의 3 제곱은 {num ** 3}입니다.'

@app.route('/cube/<int:num>')
def cube(num):
    return render_template('cube.html', html_num=num)


#실습           ##인자 두개로 넘겨줘도 상관없음
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['피자','파스타','떡볶이','짜장면','짬뽕','탕수육','볶음밥']
    order = random.sample(menu, people)
    return str(order)                       #리스트 타입은 return 할 수 없음


@app.route('/movie')
def movie():
    movies = ['토이스토리4', '알라딘', '스파이더맨', '엔드게임']
    return render_template('movie.html', movies=movies)         #리스트 타입도 넘길 수 있음


if __name__ == '__main__':
    app.run(debug=True)
