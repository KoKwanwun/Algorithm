import math

def solution(arrayA, arrayB):
    # 각각 gcd 구하기
    gcdA, gcdB = 0, 0
    for num in arrayA:
        gcdA = math.gcd(gcdA, num)
    for num in arrayB:
        gcdB = math.gcd(gcdB, num)
        
    # 서로의 숫자 카드 중 gcd로 나눠지는 것이 있다면 0 리턴
    def check(array, num):
        for i in range(len(array)):
            if array[i] % num == 0:
                return 0
        else:
            return num
    
    result = max(check(arrayA, gcdB), check(arrayB, gcdA))
    
    return result