n = int(input())

mlist = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for _ in range(1, n):
    newMlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(10):
        if(i == 0):
            newMlist[i] = mlist[1]
        elif(i == 9):
            newMlist[i] = mlist[8]
        else:
            newMlist[i] = mlist[i-1] + mlist[i+1]

    mlist = newMlist

print(sum(mlist))
