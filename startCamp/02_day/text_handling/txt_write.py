# 열기 모드
# r : 읽기, w : 쓰기(write - 오버라이트), a : 추가(append)

f = open('ssafy.txt','w')

####파일 생성후 안에 10줄 작성
for i in range(10):
    f.write(f'this is line {i + 1} \n')
f.close()       #open하고 난 다음에는 꼭 .close()해줘야함

####with 구문으로 열고 for문 돌리기
with open('with_ssafy.txt','w') as f: #컨텍스트 매니저 - 코드블럭을 만들어줘서 해당 블럭을 벗어나면 자동으로 close()됨 / with로 열었을 경우에는 반환값이 없어서 다른 변수에 할당해줄수 없음
    for i in range(10):
        f.write(f'this is line {i + 1}\n')

####오버라이트하기
with open('ssafy.txt', 'w', encoding='utf-8') as f :
    f.writelines(['0\n', '1\n', '2\n', '3\n'])
