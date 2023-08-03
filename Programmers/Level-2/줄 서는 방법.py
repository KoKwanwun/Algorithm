"""
permutations : 시간 초과 발생
from itertools import permutations

def solution(n, k):
    return list(permutations(range(1, n+1)))[k-1]
"""

# factorial 함수
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def solution(n, k):
    mlist = [i for i in range(1, n+1)]
    result = []
    
    while n > 1:
        # 인덱스를 구해주기 위해 k-1
        fac = (k-1) // factorial(n-1)
        k = k % factorial(n-1)
        result.append(mlist.pop(fac))
        n -= 1
        
    result.append(mlist[0])    
    return result