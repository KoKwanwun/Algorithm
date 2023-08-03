n = int(input())
time = list(map(int, input().split()))
time.sort()     # 오름차순 정렬을 해야만 최소를 만들 수 있음

# 누적합 구하기(현재 인덱스의 값 + 이전 인덱스의 값)
for i in range(1, n):
    time[i] += time[i-1]

# 총 걸리는 시간 출력
print(sum(time))