dinner = {
    '양자강': '02-557-4211',    #차돌짬뽕
    '김밥카페': '02-553-3181',  #라돈
    '순남시래기': '02-508-0887' #보쌈정식
}

# 1. String formatting

with open('dinner.csv','w',encoding="utf-8") as f:
    for item in dinner.items():     #[['양자강','02-557-421'], ['김밥카페', '02-553-3181'], ...] --> 딕셔너리를 리스트 형태로 바꾸기
        f.write(f'{item[0]},{item[1]}\n') #양자강, 01-557-4221

# 2. csv writer
import csv
with open('dinner.csv', 'w', encoding="utf-8", newline='') as f:                 ##윈도우에서 with open구문사용해서 파일을 열 경우 개행이 한줄씩 추가로 됨 --> newline 옵션을 따로 적어주면 해결
    csv_writer = csv.writer(f)  #f라는 파일에 csv를 작성하는 객체를 생성
    for item in dinner.items():
        csv_writer.writerow(item)
        