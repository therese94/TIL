# 딕셔너리 만들기 
lunch1 = {
    '중국집' : '02'
}
print(lunch1)

lunch2 = dict(중국집='02')
print(lunch2)


# 딕셔너리 접근하기
print(lunch1['중국집'])


# 딕셔너리 내용 추가하기
lunch1['분식집'] = '031'
print(lunch1)


# 딕셔너리 내용 가져오기
idol ={
    'bts' : {
        '지민' : 24,
        'RM' : 25
    }
}

#랩몬스터의 나이는?
print(idol['bts']['RM'])

print('==================================')


#딕셔너리 반복문 활용하기   딕셔너리를 그냥 돌리면 바로 key값이 나옴
for key in lunch1:
    print(key, lunch1[key])


#value만 가져오기
for value in lunch1.values():
    print(value)


#key만 가져오기 - 제일위 for문과 결과는 같지만 list형태로 반환하는 것이 다름
for key in lunch1.keys():
    print(key)


# .items() => key, value 가져오기
for key, value in lunch1.items():
    print(lunch1.items())
    print(key, value)