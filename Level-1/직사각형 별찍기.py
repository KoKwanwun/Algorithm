# 이중 for문을 이용한 별찍기
a, b = map(int, input().strip().split(' '))
for _ in range(b):
    for _ in range(a):
        print("*", end='')
    print()