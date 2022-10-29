n = int(input())

mlist = [0] * 46
mlist[1] = 1
mlist[2] = 1

# DP 바텀업 방식
for i in range(3, n+1):
    mlist[i] = mlist[i-1] + mlist[i-2]
    
print(mlist[n])