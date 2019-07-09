### GIT

git, DVCS (Distributed Version Control System)

원격 저장소 & 로컬 (서버 <--> 로컬)



**<u>1. GIT 장점</u>**

git을 사용할 경우 여러번 수정된 파일에서 뭐가 바뀌었는지 알수 있다.



<u>**2. GIT 작업 흐름**</u>

add				커밋할 목록에 <u>추가</u>

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

```
$ git config --global user.name "therese94"

$ git config --global user.email "theresej91@gmail.com"

$ git config --global --list	(이걸로 확인)
```



(2)  C, D드라이브가 아닌 지정 폴더(내가 원하는 폴더)로 들어간 후 (cd)

```
$ git init 	#저장소를 완전히 새로 만드는 것
```

후 확인 --> 파란색으로 (master) 나오면 된다 = git으로 관리가 되고있다는 뜻



**<u>6. GIT실습</u>**

**commit 총 두번하고 github에 올려보기



~/TIL/startCamp (master) 상태에서

```
$ git add 01_day/

$ git status

$ git commit -m "startCamp Day02"	#메시지 남기는 작업

$ git log
```

--------------------------------------------------------------------------------------------------------------------------------

여기까지 하면 어디로 push 할지는 지정해주지 않은 상태

이제부터 원격 저장소를 추가하고 지정해줘야함



이때 내 github repositories 들어가서 TIL --> http의 주소 복사



```
$ git remote -v		#원격 저장소를 다루는 키워드

$ git remote add origin https://github.com/therese94/TIL.git

$ git remote -v		#다시 확인하면 origin에 저장된 내역 보임 (fetch),(push)

$ git push origin master	#이거 치면 로그인창 뜸 --> github 계정으로 로그인
```

-------------------------------------------------------------------------------------------------------------------------------

github들어가서 해당 폴더 내역보면 commit되어있음



github내에서 수정도 가능하고 수정후 commit버튼 누르면 바로 반영됨

 (remote로만 반영, local로는 따로 가져와야함)



```
$ git pull origin master 	#맨 마지막 줄에 remote상에서 변경한 내용 나옴
```



### **push하기 전에는 pull을 해야하는지 체크해야함**

### **(충돌나지 않도록 유의)**

$ git log로 체크해보면 됨



--------------------------------------------------------------------------------------------------------------------------------



집에서 github상의 내용 다운받을때



github --> clone or download(여기서 주소 복사)









​	



