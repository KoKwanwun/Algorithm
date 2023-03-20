import math

# k진수로 변환
def convert(n, k):
    result = ""

    while n:
        result += str(n % k)
        n //= k

    return result[::-1]

# 소수 판별
def isPrime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    kNum = convert(n, k)
    mlist = str(kNum).split("0")        # 0으로 split하여 규칙에 맞게 P 리스트 생성
    result = 0

    for each in mlist:                  
        if each == '' or each == '1':   # 빈 문자열, 1일 때는 소수 아님
            continue
        if isPrime(int(each)):
            result += 1

    return result

print(solution(437674, 3))