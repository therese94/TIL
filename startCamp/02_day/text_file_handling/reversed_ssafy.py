with open('ssafy.txt','r') as f:
    lines = f.readlines()  #모든 줄을 읽어온 후에 각 줄을 리스트 형식으로 반환
    # print(lines)

lines.reverse() #list를 반대로 뒤집는다.

with open('reversed_ssafy.txt','w') as f:
    for line in lines:
        f.write(line)


# reversed_lines = lines.reverse()
# for i in lines:
#     print(reversed_lines[i])

# f2 = open('reversed_text.txt','w')
# for i in range(4):
#     f2.write(i)
# for i in range(len(reversed_lines)):
#     f2.write(reversed_lines[i])

# f2.close()