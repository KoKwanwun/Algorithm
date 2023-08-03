n, k = map(int, input().split())
mlist = list(map(int, input().split()))

# 슬라이싱 sum(mlist[i:i+k])으로 한다면 시간초과
sumList = [sum(mlist[0:0+k])]
for i in range(1, n-k+1):
    sumList.append(sumList[i-1] - mlist[i-1] + mlist[i+k-1])

print(max(sumList))