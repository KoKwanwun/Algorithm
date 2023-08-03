# combinations를 이용한 조합 리스트
# prime_check로 소수 여부 체크

from itertools import combinations

def solution(nums):
    answer = 0
    
    def prime_check(n):
        c = [False,False] + [True]*(n-1)
        for i in range(2, n+1):
            if c[i] == True:
                for j in range(2*i, n+1, i):
                    c[j] = False
        return c

    prime_list = prime_check(50000)

    for i in combinations(nums,3):
        if prime_list[sum(i)]:
            answer += 1

    return answer