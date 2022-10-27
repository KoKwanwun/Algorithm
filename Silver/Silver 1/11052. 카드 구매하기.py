import sys

n = int(input())

card = list(map(int, sys.stdin.readline().split()))
card.insert(0, 0)

d = [-1] * (n+1)

d[0] = 0

for i in range(1, n+1):
    for j in range(i, n+1):
        if(d[j-i] != -1):
            d[j] = max(d[j], d[j-i] + card[i])

print(d)