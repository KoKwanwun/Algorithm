# 이 문제는 에라토스테네스의 체를 쓰면 더 오래걸리는 것 같음
n = int(input())

# 에라토스테네스의 체
sieve = [False, False] + [True] * (n-1)
primes = []

for i in range(2, n+1):
    if(sieve[i]):
        primes.append(i)
        for j in range(2*i, n+1, i):
            sieve[j] = False

# 소인수분해
while n != 1:
    for i in range(len(primes)):
        if(n % primes[i] == 0):
            print(primes[i])
            n //= primes[i]
            break