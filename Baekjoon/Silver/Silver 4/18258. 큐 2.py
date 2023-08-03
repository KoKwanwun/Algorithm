import sys
from collections import deque

input = sys.stdin.readline
dq = deque()

# 각 명령어에 맞게 실행
for _ in range(int(input())):
    strs = input()

    if strs.startswith("push"):
        push, num = strs.split()
        dq.append(int(num))
    elif strs.startswith("pop"):
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif strs.startswith("size"):
        print(len(dq))
    elif strs.startswith("empty"):
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif strs.startswith("front"):
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif strs.startswith("back"):
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])