n = int(input())

mlist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for _ in range(1, n):
    for i in range(10):
        print(sum(mlist[i:9]))
        mlist[i] = sum(mlist[i:10])

print(sum(mlist) % 10007)