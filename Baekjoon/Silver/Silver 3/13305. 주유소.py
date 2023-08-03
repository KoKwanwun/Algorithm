N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

# 초기값 설정
minPrice = price[0]
result = price[0] * road[0]

# minPrice 갱신 후, result에 더해가기
for i in range(1, N-1):
    if minPrice > price[i]:
        minPrice = price[i]
    result += road[i] * minPrice

print(result)