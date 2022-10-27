import sys

n, m = map(int, sys.stdin.readline().split())

mlist = []

mlist.append([0] * (m+1))

for _ in range(n):
    s = list(map(int, sys.stdin.readline().split()))
    s.insert(0, 0)
    mlist.append(s)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        mlist[i][j] += max(mlist[i-1][j], mlist[i-1][j-1], mlist[i][j-1])

print(mlist[n][m])