from itertools import product

a, b = map(int, input().split())
result = 0

for i in range(len(str(a)), len(str(b))+1):
    # 자리수만큼 경우의 수
    # repeat = 1 : [(4,), (7,)]
    # repeat = 2 : [(4, 4), (4, 7), (7, 4), (7, 7)]
    tmp = list(product([4, 7], repeat = i))

    for num in tmp:
        # 정수 변환
        n = int(''.join(map(str, num)))
        if a <= n and n <= b:
            result += 1

print(result)