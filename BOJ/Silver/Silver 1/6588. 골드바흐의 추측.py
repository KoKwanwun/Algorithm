import sys

# 에라토스테네스의 체
sieve = [False, False] + [True] * (1000000)

for i in range(2, 1000000):
    if(sieve[i]):
        for j in range(2*i, 1000000, i):
            sieve[j] = False

while(True):
    n = int(sys.stdin.readline())
    
    if(n == 0):
        break

    # for-else문 : for문이 break없이 완료되면 else문 실행
    for i in range(3, n+1, 2):          # 홀수만 체크
        if(sieve[i] and sieve[(n-i)]):
            print(n, "=", i, "+", (n-i))
            break  
    else:
        print("Goldbach's conjecture is wrong.")
        break
