##########500개 파일(.txt파일) 이름 앞에 SAMSUNG 붙이기
##########SAMSUNG 대신 SSAFY로 바꾸기
import os

# 500개의 파일이 있는 디렉토리로 이동
os.chdir(r"C:\Users\student\TIL\startCamp\02_day")  #parameter로 경로를 가짐

# 파일의 목록을 전부 가져오는 함수 사용
filenames = os.listdir('.')    #특정경로에 있는 모든 파일 이름을 가져옴 --> .은 현재 경로를 뜻함


for filename in filenames:
    extension = os.path.splitext(filename)[-1]    #os.path.splitext()라는 함수를 이용해 확장자만 따로 분리 --> extension에 담긴것들은   tuple이라는 자료구조인데 이것도 index로 접근가능

    # 확장자가 .txt 인 파일만 이름을 바꾼다.
    if extension=='.txt':
        # os.rename(filename, f'SAMSUNG_{filename}')     #첫번째 인자로 넘어간 이름을 두번째 인자로 넘어간 이름으로 바꾼다.
        os.rename(filename, filename.replace("SAMSUNG_","SSAFY_"))

