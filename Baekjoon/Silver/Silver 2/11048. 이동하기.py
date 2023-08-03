import sys

n, m = map(int, sys.stdin.readline().split())

mlist = []

# 1행, 1열에 각각 0 한줄을 넣어줌
"""
2*2 배열이라면 아래처럼 추가하여 index overflow 방지
0 0 0
0
0
"""
mlist.append([0] * (m+1))
for _ in range(n):
    s = list(map(int, sys.stdin.readline().split()))
    s.insert(0, 0)
    mlist.append(s)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        mlist[i][j] += max(mlist[i-1][j], mlist[i-1][j-1], mlist[i][j-1])

print(mlist[n][m])