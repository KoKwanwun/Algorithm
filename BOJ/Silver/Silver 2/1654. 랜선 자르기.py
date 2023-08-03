# 파라메트릭 서치(Parametric Search)
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
mlist = [ int(input()) for _ in range(k) ]

left, right = 1, max(mlist)

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for each in mlist:
        cnt += each // mid

    if cnt >= n:
        left = mid + 1
    else:
        right = mid - 1
    # left와 right가 같은 지점이 결과값이 됨

print(right)