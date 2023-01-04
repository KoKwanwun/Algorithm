def solution(n):
    # 피보나치 수열 활용
    mlist = [0] * 2000
    
    mlist[0] = 1
    mlist[1] = 2
    
    for i in range(2, n):
        mlist[i] = mlist[i - 1] + mlist[i - 2]
    
    return mlist[n - 1] % 1234567