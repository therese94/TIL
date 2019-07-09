# 1. split
with open('dinner.csv', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip().split(','))         ##개행문자 추가된거 없애줌, ','기준으로 문자열 나눔

# 2. csv reader
import csv
with open('dinner.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)