import sys
input = sys.stdin.readline

n, k = map(int, input().split())
mlist = [list(map(int, input().split())) for _ in range(n)]

# 3과목이 있으므로 2개를 뽑아서 최대값 구하기
# 0, 1 과목 합이 큰 순서대로 정렬 후 k개 뽑기
result = 0
for a, b, c in sorted(mlist, key = lambda x : -(x[0] + x[1]))[0:k]:
    result += (a + b)

# 1, 2 과목 합이 큰 순서대로 정렬 후 k개 뽑기
result = 0
tmp = 0
for a, b, c in sorted(mlist, key = lambda x : -(x[1] + x[2]))[0:k]:
    tmp += (b + c)
result = max(result, tmp)

# 0, 2 과목 합이 큰 순서대로 정렬 후 k개 뽑기
result = 0
tmp = 0
for a, b, c in sorted(mlist, key = lambda x : -(x[0] + x[2]))[0:k]:
    tmp += (a + c)
result = max(result, tmp)

# 최대값 출력
print(result)