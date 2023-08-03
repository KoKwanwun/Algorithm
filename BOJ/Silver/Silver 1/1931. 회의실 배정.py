meet = []

for i in range(int(input())):
    meet.append(list(map(int, input().split())))

# 끝나는 시간으로 정렬하면 쉽게 해결 가능
earlyEnd = sorted(meet, key = lambda x : (x[1], x[0]))

result = 1
maxVal = earlyEnd[0][1]

# 최대 끝나는 시간과 각 회의의 시작 시간을 비교하며 구하기
for i in range(1, len(earlyEnd)):
    if(earlyEnd[i][0] >= maxVal):
        maxVal = earlyEnd[i][1]
        result += 1

print(result)