n = int(input())
num = 1

while True:
    # 분해합 구하기
    tmp = num + sum(list(map(int, str(num))))

    # 탈출 조건
    if num > 1000000:
        print(0)
        break

    # 찾았다면 출력하고 탈출
    if n == tmp:
        print(num)
        break

    num += 1