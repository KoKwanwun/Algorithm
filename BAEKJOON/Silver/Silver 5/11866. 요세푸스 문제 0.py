from collections import deque

n, k = map(int, input().split())
dq = deque()
result = []

# deque에 넣기
for i in range(1, n+1):
    dq.append(i)

# 요세푸스 순열로 돌리기
tmp = k
while dq:
    tmp -= 1
    if tmp == 0:
        result.append(str(dq.popleft()))
        tmp = k
    else:
        dq.append(dq.popleft())

print('<' + ', '.join(result) + '>')