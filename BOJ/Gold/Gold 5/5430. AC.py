# 매번 R이 있을때 reverse 해주면 시간 초과
from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    methods = list(input().rstrip())
    cnt = int(input())
    # 리스트 형태 입력받아 deque에 넣기
    mlist = deque(input().rstrip()[1:-1].split(","))
    flag = 0

    # D의 개수가 원소 개수보다 많다면 error
    if cnt < methods.count("D"):
        print("error")
    else:
        # flag가 짝수면 popleft, 홀수면 pop
        for method in methods:
            if method == "R":
                flag += 1
            else:
                if flag % 2 == 0:
                    mlist.popleft()
                else:
                    mlist.pop()

        # 출력시에도 flag 반영
        if flag % 2 == 0:
            print("[" + ",".join(mlist) + "]")
        else:
            mlist.reverse()
            print("[" + ",".join(mlist) + "]")