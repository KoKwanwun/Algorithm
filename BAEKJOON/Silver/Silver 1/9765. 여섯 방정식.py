# 최대공약수로 풀었다면 시간을 엄청 줄일 수 있었다고 생각이 든다..
# 소인수분해
def factorization(x):
    d = 2
    returnList = []

    while d <= x:
        if x % d == 0:
            x //= d
            returnList.append(d)
            returnList.append(x)
            return returnList
        else:
            d += 1

c1, c2, c3, c4, c5, c6 = map(int, input().split())

c1List = factorization(c1)
c3List = factorization(c3)

if c5 % c1List[0] == 0:
    x2 = c1List[0]
    x1 = c1List[1]
    x3 = c5 // c1List[0]
else:
    x2 = c1List[1]
    x1 = c1List[0]
    x3 = c5 // c1List[1]

if c6 % c3List[0] == 0:
    x6 = c3List[0]
    x7 = c3List[1]
    x5 = c6 // c3List[0]
else:
    x6 = c3List[1]
    x7 = c3List[0]
    x5 = c6 // c3List[1]

print(x1, x2, x3, x5, x6, x7)