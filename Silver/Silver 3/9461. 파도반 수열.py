mlist = [0] * 101
mlist[1] = 1
mlist[2] = 1
mlist[3] = 1

for i in range(4, 101):
    mlist[i] = mlist[i-2] + mlist[i-3]
  
t = int(input())

for i in range(t):
    n = int(input())
    print(mlist[n])