### GIT

git, DVCS (Distributed Version Control System)

원격 저장소 & 로컬 (서버 <--> 로컬)



**<u>1. GIT 장점</u>**

git을 사용할 경우 여러번 수정된 파일에서 뭐가 바뀌었는지 알수 있다.



<u>**2. GIT 작업 흐름**</u>

add				커밋할 목록에 추가

commit		커밋(create a sanpshot)만들기

push			 현재까지의 역사(commits)가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기



**어떤코드만 커밋할지도 정할 수 있음

**내가 남긴 커밋을 보고 팀원이 팔로우업 가능



**<u>3. GIT 기본</u>**

$ git add helloworld.py						(git의 sub-command 중 하나)

$ git commit -m

$ git config --global user.name "John"			(보통 --로 시작하명 long name옵션)



**<u>4. GIT초기화 - 엄청 중요한거</u>**

(1) git bash실행 후, 미리 설정되어있을지 모를 계정 정보 삭제(처음 설치 생략 가능)

(2) windows 자격 증명 과리자에서 git관련 정보 삭제

(3) git bash 실행 후 아래와 같이 입력

```
$ git credentail reject

protocol = https

host =github.com
```



<u>**5. GIT 설정**</u>

(0) git bash를 켠다

(1) git 계정 정보 등록 --> 아이디, 이메일

​	$ git config --global user.name "therese94"

​	$ git config --global user.email "theresej91@gmail.com"

​	$ git config --global --list	(이걸로 확인)

(2)  C, D드라이브가 아닌 지정 폴더(내가 원하는 폴더)로 들어간 후 (cd)

​	$ git init 

후 확인 --> 파란색으로 (master) 나오면 된다



**<u>6. GIT실습</u>**

**commit 총 두번하고 github에 올려보기



~/TIL/startCamp (master) 상태에서

$ git add 01_day/

$ git status

$ git log

​	



