import sys

while(True):
    x, y = map(int, sys.stdin.readline().split())

    # x, y 둘다 0일 경우 탈출
    if(x == 0 and y == 0):
        break

    print(x + y)