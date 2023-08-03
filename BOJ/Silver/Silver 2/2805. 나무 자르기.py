import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mlist = list(map(int, input().split()))

left, right = 1, max(mlist)
while left <= right:
    mid = (left + right) // 2
    total = 0
    for each in mlist:
        if each > mid:
            total += each - mid

    if total >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)