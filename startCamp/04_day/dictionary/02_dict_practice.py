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

sum = 0
for value in score.values():
    sum += int(value)

result = sum/3
print(f'평균은 {result}입니다.')



# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
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
print('\n')
print('==== Q2 ====')

result1 = 0
result2 = 0

for key in scores['a']:
    result1 += int(scores['a'][key])

for key in scores['b']:
    result2 += int(scores['b'][key])

result1 = result1/3
result2 = result2/3

print(f'a 평균은 {result1}입니다.')
print(f'b 평균은 {result2}입니다.')
print(f'두 사람의 평균은 {(result1 + result2)/2}입니다.')


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('\n')
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
i = 0
sum_tem = 0
result_tem = []
ave = 0

for value in city.values():
    for n in range(3):
        sum_tem += int(value[n])
    ave = sum_tem/3
    result_tem.append(ave)
    sum_tem = 0

for key in city:
    print(f'{key} : {result_tem[i]}')
    i += 1



# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('\n')
print('==== Q3-2 ====')

# temp1 = ''
# temp2 = ''
# city_h = result_tem[0]
# city_c = result_tem[0]

# for i in result_tem():
#     for j in range(1,i):
#         if i < result_tem[j]:
#             city_h = result

city2 = {
    '서울': result_tem[0],
    '대전': result_tem[1],
    '광주': result_tem[2],
    '부산': result_tem[3],
}

print(city2)

# city_h = city2[max(result_tem)]
# city_c = city2[min(result_tem)]

# city_h = max(result_tem)
# city_c = min(result_tem)


# print(f'가장 더웠던곳은 {city_h}입니다.')
# print(f'가장 추웠던곳은 {city_c}입니다.')


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('\n')
print('==== Q3-3 ====')


def isDegree():
    count = 0
    for j in city['서울']:
        if j >= 2:
            print('네 있습니다')
            break
        else:
            count += 1
            if count == 3:   
                print('없습니다.')    

isDegree()