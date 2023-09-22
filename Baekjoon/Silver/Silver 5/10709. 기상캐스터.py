h, w = map(int, input().split())

for _ in range(h):
    mlist = list(input())
    tmp = -1
    for each in mlist:
        if each == 'c':
            tmp = 0
            print(tmp, end=' ')
        else:
            if tmp == -1:
                print(tmp, end=' ')
            else:
                tmp += 1
                print(tmp, end=' ')
    print()