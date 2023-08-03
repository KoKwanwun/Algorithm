n, m = map(int, input().split())

if n == 1:                          # 이동 불가
    print(1)
elif n == 2:                        # 4번 이상 이동 불가하며, m의 값에 따라 2, 3번의 방법을 사용하여 min값
    print(min(4, (m + 1) // 2))
else:                               # 4가지 방법을 사용하기 위해 m이 7이상이어야 함
    if m <= 6:
        print(min(4, m))
    else:                           # 4가지 방법을 다 사용할 때, 오른쪽으로 2칸 가는 것 2번 나머지는 오른쪽으로 1칸이므로 -2 해줌
        print(m-2)