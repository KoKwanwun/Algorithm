# 제한 조건이 1,000,000이기 때문에 인덱스가 소수인 값에 true
# true는 1이기 때문에 sum으로 개수 리턴
def prime_check(n):
    c = [False,False] + [True]*(n-1)
    for i in range(2, n+1):
        if c[i] == True:
            for j in range(2*i, n+1, i):
                c[j] = False
    return c

def solution(n):
    prime_list = prime_check(1000000)

    return sum(prime_list[2:n+1])