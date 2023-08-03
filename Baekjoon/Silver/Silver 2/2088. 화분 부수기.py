import sys

mlist = []
n = int(sys.stdin.readline())
for _ in range(n):
    mlist.append(list(map(int, sys.stdin.readline().split())))

# dp 활용 방문한 숫자를 체크
dp = [0] * 1000001

result = 0
for a, b, c in mlist:
    if not dp[a] and not dp[b] and not dp[c]:
        result += 1
    dp[a] = 1
    dp[b] = 1
    dp[c] = 1

print(result)