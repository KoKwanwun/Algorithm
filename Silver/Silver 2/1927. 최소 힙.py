# heapq 사용하여 최소 힙
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
            print(heappop(mlist))
    else:
        heappush(mlist, tmp)