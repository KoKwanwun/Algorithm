n = int(input())
mlist = list(map(int, input().split()))
reverseMlist = list(reversed(mlist))
upDp = [0] * n
downDp = [0] * n
result = [0] * n

# 증가하는 수열은 일반적으로, 감소하는 수열은 reverse한 후 증가하는 수열을 구한 후 다시 reverse 시켜줌 (감소 = reverse 증가)
"""
- reverse를 해야하는 이유
mlist	1 5 2 1 4 3 4 5 2 1
up	    1 2 2 1 3 3 4 5 2 1
down	1 1 2 3 2 3 2 1 4 5
reverse 1 5 2 1 4 3 3 3 2 1

up과 down은 증가, 감소를 찾아야하기 때문에 오름차순
reverse증가reverse는 거꾸로 증가하는 최대값이기 때문에 바이토닉 부분 수열을 구할 수 있음
-> -1을 해주는 이유는 최대값을 더해줄 때, 1개가 겹치기 때문
"""
# 이후 각 인덱스에 있는 최대값을 더해준 후 1을 빼서 result 리스트를 생성해줌
for i in range(n):
    for j in range(i):
        if(mlist[i] > mlist[j] and upDp[i] < upDp[j]):
            upDp[i] = upDp[j]
        if(reverseMlist[i] > reverseMlist[j] and downDp[i] < downDp[j]):
            downDp[i] = downDp[j]
    upDp[i] += 1
    downDp[i] += 1

downDp = list(reversed(downDp))
        
for i in range(n):
    result[i] = upDp[i] + downDp[i] - 1

print(max(result))