n = int(input())

mlist = [0] * (n+1)
mlist[1] = 1

for i in range(2, n+1):
    mlist[i] = mlist[i-2] + mlist[i-1]
   
print(mlist[n])