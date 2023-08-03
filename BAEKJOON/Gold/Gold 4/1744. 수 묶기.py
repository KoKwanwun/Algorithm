# 양수, 음수, 0을 나누어 저장
positiveNum = []
negativeNum = []
zeroNum = []

for i in range(int(input())):
    num = int(input())

    if(num > 0):
        positiveNum.append(num)
    elif(num < 0):
        negativeNum.append(num)
    else:
        zeroNum.append(num)

# 절대값이 큰 순으로 정렬
positiveNum.sort(reverse=True)
negativeNum.sort()

result = 0

# 양수
for i in range(0, len(positiveNum), 2):
    if(i == len(positiveNum)-1):                            # 개수가 홀수라면 그냥 덧셈
        result += positiveNum[i]
    elif(positiveNum[i] == 1 or positiveNum[i+1] == 1):     # 묶을 때 둘 중 1이 있다면 그냥 덧셈
        result += positiveNum[i]
        result += positiveNum[i+1]
    else:                                                   # 그 외는 묶기
        result += (positiveNum[i] * positiveNum[i+1])

# 음수
for i in range(0, len(negativeNum), 2):
    if(i == len(negativeNum)-1):                            # 개수가 홀수라면, 하나의 음수가 남는데 -> 0이 존재한다면 넘어가고, 아니라면 음수 덧셈
        if(len(zeroNum) > 0):
            continue
        else:
            result += negativeNum[i]
    else:                                                   # 음수의 곱은 양수므로 곱해주기
        result += (negativeNum[i] * negativeNum[i+1])

print(result)