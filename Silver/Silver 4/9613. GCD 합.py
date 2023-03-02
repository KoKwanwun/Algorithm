from itertools import combinations

# 유클리드 호제법 : 최대공약수
def GCD(x, y):
    while(x % y != 0):
        x, y = y, x % y

    return y

for _ in range(int(input())):
    mlist = list(map(int, input().split()[1:]))
    sumVal = 0

    # 모든 조합의 GCD의 합 구하기
    for each in combinations(mlist, 2):
        sumVal += GCD(each[0], each[1])

    print(sumVal)