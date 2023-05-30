import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    mlist = list(map(int, sys.stdin.readline().split()))

    # enumerate 함수를 사용하여 현재 인덱스 저장
    dq = deque(enumerate(mlist))
    order = 1

    while dq:
        tmp = dq.popleft()

        #  현재 문서보다 중요한 문서가 존재한다면 queue에 다시 추가
        # 그 외는 찾고 있는 데이터라면 출력, 아니라면 순서 +1
        for i, data in dq:
            if data > tmp[1]:
                dq.append(tmp)
                break
        else:
            if tmp[0] == m:
                print(order)
            else:
                order += 1