# 카드 숫자의 가장 크고 작은 수의 절댓값인 10000000의 +1개만큼의 리스트 생성
mlist = [0] * 10000001
result = []

# 상근이가 가지고 있는 숫자 카드가 양수일 때는 해당 인덱스의 +1, 음수일 때는 해당 인덱스의 +2
n = int(input())
for num in list(map(int, input().split())):
    if num >= 0:
        mlist[num] += 1
    else:
        mlist[abs(num)] += 2

# 1인 경우 : 양수만
# 2인 경우 : 음수만
# 3인 경우 : 양수 음수 둘다
m = int(input())
for num in list(map(int, input().split())):
    if num >= 0:
        if mlist[num] == 1 or mlist[num] == 3:
            result.append('1')
        else:
            result.append('0')
    else:
        if mlist[abs(num)] == 2 or mlist[abs(num)] == 3:
            result.append('1')
        else:
            result.append('0')

print(' '.join(result))