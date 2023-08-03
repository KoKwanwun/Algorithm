from collections import Counter

n = int(input())
mlist = Counter(list(map(int, input().split())))

result = 1
for value in mlist.values():
    result *= (value + 1)

# 전부 안뽑는 경우 1개를 제외
print((result - 1) % (10 ** 9 + 7))

"""
Counter를 사용하지 않는 방법
table = {}
for i in arr:
    if i not in table:
        table[i] = 1
    else :
        table[i] += 1
"""