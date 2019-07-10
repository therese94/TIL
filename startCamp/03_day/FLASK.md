**FLASK**

(0) vs code 왼쪽 아이콘 --> 검색 --> live server에서 install하기 / jinja2 template language..? 찾아보기(끝부분에 필기)

(1) 구글에서 검색해서 페이지 들어가기 http://flask.pocoo.org/



(2) git bash에 

```
pip install Flask
```

입력해서 다운받기



(3) 폴더 만들기 & 정리

flask --> intro --> py파일 하나 만들기

py 파일 안에   flask 홈페이지의 flask is fun 부분 복사해서 붙이기

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```



터미널 창에 and easy to setup 부분 코드 복붙해서 실행(밑에 코드)

```python
FLASK_APP=hello.py flask run
```



<u>ctrl + 주소 눌러서 들어가기</u>

ctrl + c 눌러서 밖으로 나오기



**파일 이름을 app.py로 해놓으면 그냥 $ flask 만 쳐도 실행됨

**flask 서버는 라이브가 아니라서 뭔가 수정하면 그때그때 재실행 해야함

***수정시 서버 자동 재부팅 기능 있음

```python
app.run(debug=True)
```

*********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************

python app.py로 직접 호풀시에만 서버로 사용하기 위함 --> 기본적으로  python모듈에는 //__name__//이 있는데 ~~

----------------------------------------------------------------------------------------------------------------------------------------------------------------



서버 주소 뒤에 /치고 정한 이름(?) 입력하면 해당 함수 실행

```python
@app.route('/greeting/ziont')
def greeting_ziont():
    return '반갑습니다 ZionT님'
```

**<u>Variable Routing</u>**

```python
# Variable Routing
@app.route('/greeting/<name>')
def greeting(name):
    return f'반갑습니다. {name} 님' 
```

url 에서 variable을 받을 수 있음(기본적으로 str타입으로 받음)



**python 팁

같은(비슷한) 키워드끼리 동시 선택 --> ctrl + d	/	벗어나기 --> esc 

ctl + p --> 파일 찾기



**gitignore 생성 팁

https://www.gitignore.io/ 

들어가면 편하게 만들 수 있음

--> 메인 조건창에 flask, windows, python, visual studio code 등 입력하고 들어가서 전체 복사



TIL 폴더로 visual studio code열기 하면 .gitignore파일이 있음 --> 거기에 전체 붙여넣기 & save

---------------------------------------------------------------------------------------------------------

**중요**

app.py와 동일한 경로에 꼭 'templates'라는 이름으로 폴더 만들기

--> 내부에 html 파일 만들거

**render_template 추가하기 (이걸로 html페이지 보여줄 수 있음)

```python
from flask import Flask, render_template
import datetime
import random
app = Flask(__name__)

@app.route("/")@app.route()는 endpoint 기능
def hello():
    return render_template('index.html')
```

**반환문에 render_template함수로 index.html 보여줄수 있도록 작성

**index.html 작성할때 			! + tab 	or	 html:5 + tab 



-------------------------------------------------------------------------------------

**<u>jinja2 template language</u>**

example 1

```html
<body>	
    {% if html_name == 'June' %}		<--> 템플릿 태그</-->
        <h1>{{ html_name }}님 오셨습니까?</h1>
    {% else %}
        <h1>{{ html_name }} 왔니..?</h1>    
    {% endif %}
</body>
```

example 2

```html
<body>
    <h1>영화 목록</h1>
    <ul>
    {% for movie in movies %}
        <li>{{ movie }}</li>
    {% endfor %}
    </ul>
</body>
```

**주의할점 :  {% %}는 주석 안에 있어도 해석됨(굳이 써야하면 밑처럼 쓰기)

<!-- {# #} -->