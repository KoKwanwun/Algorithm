# 슬라이딩 윈도우 : DP에서 메모이제이션을 할 때, 사용하지 않는 값을 배열에 저장하지 않고 배열을 새롭게 계속해서 갱신시켜주는 것
# 발상의 전환 : DP를 사용하여 입력받은 것의 max, min 값이 아닌, DP의 max, min 값을 사용
import sys
input = sys.stdin.readline

n = int(input())
mlist = list(map(int, input().split()))
maxDp = mlist
minDp = mlist

for _ in range(n-1):
    mlist = list(map(int, input().split()))
    maxDp = [mlist[0] + max(maxDp[0], maxDp[1]), mlist[1] + max(maxDp), mlist[2] + max(maxDp[1], maxDp[2])]
    minDp = [mlist[0] + min(minDp[0], minDp[1]), mlist[1] + min(minDp), mlist[2] + min(minDp[1], minDp[2])]
    
print(maxDp)
print(minDp)