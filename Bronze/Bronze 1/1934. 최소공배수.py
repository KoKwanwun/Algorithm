for i in range(int(input())):
    x, y = map(int, input().split())
    multiXY = x * y

    while x % y != 0:
        x, y = y, x % y

    print(multiXY // y)