n, m = map(int, input().split())

strs = []
result = 0

# 문자열 집합 만들기
for i in range(n):
    strs.append(input())

# 포함 여부 확인 후, result에 반영
for i in range(m):
    tmp = input()
    if tmp in strs:
        result += 1

print(result)