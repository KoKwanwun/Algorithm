# 다마고치의 체력이 1인 상태로 먹이를 1개씩 주면
# 최소한의 먹이로 생존이 가능함 ( 낮에는 2, 밤에는 1로 바뀜 )
for _ in range(int(input())):
    n, m = map(int, input().split())

    cnt = 0
    while n:
        n //= 2
        cnt += 1

    print(cnt + m)