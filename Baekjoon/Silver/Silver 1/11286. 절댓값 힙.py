# heapq 사용하여 절댓값으로 heap만들고 따로 원소 보관
import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
mlist = []

for i in range(n):
    tmp = int(sys.stdin.readline())

    if tmp == 0:
        if mlist == []:
            print(0)
        else:
            print(heappop(mlist)[1])
    else:
        heappush(mlist, (abs(tmp), tmp))