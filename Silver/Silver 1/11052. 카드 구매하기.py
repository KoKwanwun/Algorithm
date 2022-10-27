import sys

n = int(input())

# 인덱스가 카드팩 내의 카드 개수가 되도록 인덱스 0에 0값 추가
card = list(map(int, sys.stdin.readline().split()))
card.insert(0, 0)

# 우리는 큰 값을 구해야하므로 -1로 초기화
d = [-1] * (n+1)

d[0] = 0

for i in range(1, n+1):
    for j in range(i, n+1):
        # (j-i) 카드를 구매할 수 있는 경우, 현재 가격, j-i의 가격 + 카드가격 중 더 높은 것으로 현재값 갱신
        if(d[j-i] != -1):
            d[j] = max(d[j], d[j-i] + card[i])

# 최종적으로 카드 N개를 구매할 수 있는 최대 가격이 나옴
print(d[n])