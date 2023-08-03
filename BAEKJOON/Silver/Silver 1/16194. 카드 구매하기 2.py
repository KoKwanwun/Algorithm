n = int(input())

cost = list(map(int, input().split()))
cost.insert(0, 0)

# 우리는 작은 값을 구해야하므로 10001로 초기화
d = [10001] * (n+1)

d[0] = 0

for i in range(1, n+1):
    for j in range(i, n+1):
        # (j-i) 카드를 구매할 수 있는 경우, 현재 가격, j-i의 가격 + 카드가격 중 더 낮은 것으로 현재값 갱신
        if(d[j-i] != 10001):
            d[j] = min(d[j], d[j-i] + cost[i])

# 최종적으로 카드 N개를 구매할 수 있는 최소 가격이 나옴
print(d[n])