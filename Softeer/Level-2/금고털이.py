import sys
input = sys.stdin.readline

w, n = map(int, input().split())
# 가격 순으로 내림차순
prices = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x : -x[1])
result = 0

for price in prices:
    if w <= 0:
        break
    
    # 남아 있는 가방 무게가 보석 가격보다 크다면
    if price[0] <= w:
        result += (price[0] * price[1])
        w -= price[0]
    else:
        result += (w * price[1])
        w = 0

print(result)