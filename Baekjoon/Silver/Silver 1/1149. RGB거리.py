n = int(input())

# 초기값 설정
minList = list(map(int, input().split()))

# 현재값을 기준으로 이전 값들의 합 중 자신의 인덱스를 제외한 값의 최소값을 더해서 초기화
for i in range(n - 1):
    rgb = list(map(int, input().split()))
    i = rgb[0] + min(minList[1], minList[2])
    j = rgb[1] + min(minList[0], minList[2])
    k = rgb[2] + min(minList[0], minList[1])
    minList = [i, j, k]     # i, j, k로 값을 받고 다시 초기화한 이유 : 바로 값을 바꾸면 다른 값에 영향을 주기 때문에

print(min(minList))