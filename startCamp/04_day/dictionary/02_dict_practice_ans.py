"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

total_score = 0

for subject_score in score.values():
    total_score += subject_score

average_score = total_score/len(score.values())

print(average_score)


# 2. 반 평균을 구하시오. -> 전체 평균
scores = {                  # 딕셔너리 안에 키,딕셔너리
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

total_score = 0
count = 0

for person_score in scores.values():   # person_score 자체도 dictionary
    total_score +=sum(person_score.values())
    count += len(person_score)                  #########여기 주의하기

total_average = total_score/count
print(total_average)



# 3. 도시별 최근 3일의 온도입니다.
city = {                                # 딕셔너리 안에 키, 리스트
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""

for key, value in city.items():
    average_temp = sum(value) / len(value)
    print(f'{key} : {average_temp}')



# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?                ###SLACK에 코드 공유

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')





# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')