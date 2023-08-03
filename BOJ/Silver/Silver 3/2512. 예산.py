import sys
input = sys.stdin.readline

n = int(input())
mlist = list(map(int, input().split()))
m = int(input())

left, right = 1, max(mlist)
while left <= right:
    mid = (left + right) // 2
    total = 0
    for each in mlist:
        if each > mid:
            total += mid
        else:
            total += each

    if total > m:
        right = mid - 1
    else:
        left = mid + 1
    print(left, right)

print(right)