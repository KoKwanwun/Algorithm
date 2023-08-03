import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
scores = [ list(map(int, input().split())) for _ in range(N) ]
klist = sorted(scores, key = lambda x : (-x[1], -x[0]))

# 본상은 심판의 상위 K로 고정
result = 0
for i in range(K):
    result += klist[i][0]
klist = klist[K:]

# 특별상은 본상을 제외한 후 가장 높은 M개 선정
mlist = sorted(klist, key = lambda x : (-x[0], -x[1]))
for i in range(M):
    result += mlist[i][0]

print(result)