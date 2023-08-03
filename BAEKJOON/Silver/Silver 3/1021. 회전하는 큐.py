# 찾는 숫자 인덱스를 구한 후 어느 방향으로 회전시키는게 빠른지 찾기
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
dq = deque(list(range(1, n+1)))
result = 0

for num in list(map(int, sys.stdin.readline().split())):
    idx = dq.index(num)

    if idx <= (len(dq) // 2):
        for _ in range(idx):
            dq.append(dq.popleft())
            result += 1
    else:
        for _ in range(len(dq) - idx):
            dq.appendleft(dq.pop())
            result += 1

    dq.popleft()

print(result)