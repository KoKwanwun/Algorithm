# 피보나치 수열 구하기
def solution(n):
    mlist = []
    mlist.append(0)
    mlist.append(1)
    
    for i in range(2, n + 1):
        mlist.append(mlist[i-2] + mlist[i-1])
    
    return mlist[n] % 1234567