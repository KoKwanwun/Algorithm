n = int(input())

for _ in range(n):
    m = int(input())
    
    mlist = [0, 1, 2, 4]

    for i in range(4, m+1):
        mlist.append(mlist[i-3] + mlist[i-2] + mlist[i-1])

    print(mlist[m] % 10007)